from django.shortcuts import render, redirect
from django.http import HttpResponse

class Tutorial:
    def __init__(self, name, file, type, hint = None, existingGroups=False):
        self.name = name
        self.file = file
        self.type = type
        self.existingGroups = existingGroups
        self.hint = hint
        self.submissions = []

    def add_submission(self, submission):
        self.submissions.append(submission)

def make_admin_tutorial(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        hint = request.POST.get('hint')
        tutorial_type = request.POST.get('ass_type')
        existing_groups = request.POST.get('groups') == 'yes'
        uploaded_file = request.FILES.get('fileUpload')

        # Create instance of your Tutorial class
        tutorial = Tutorial(
            name=name,
            file=uploaded_file,
            type=tutorial_type,
            hint=hint,
            existingGroups=existing_groups
        )

        # Store the relevant data in session
        request.session['tutorial_data'] = {
            'name': tutorial.name,
            'file_name': tutorial.file.name if tutorial.file else 'No file uploaded',
            'type': tutorial.type,
            'hint': tutorial.hint,
            'existingGroups': tutorial.existingGroups
        }

        return redirect('success')
    return render(request, 'admin_tutorial.html')

def display_success(request):
    tutorial_data = request.session.get('tutorial_data')
    return render(request, 'success.html', {'tutorial': tutorial_data})