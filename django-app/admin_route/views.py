from django.shortcuts import render, redirect
from django.http import HttpResponse

class Tutorial:
    def __init__(self, name, file, file_name, type, subject, hint = None, existingGroups=False):
        self.name = name
        self.file = file
        self.file_name = file_name
        self.type = type
        self.existingGroups = existingGroups
        self.hint = hint
        self.submissions = []
        self.subject = subject

    def add_submission(self, submission):
        self.submissions.append(submission)

saved_tutorials = []

def make_admin_tutorial(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        hint = request.POST.get('hint')
        tutorial_type = request.POST.get('ass_type')
        existing_groups = request.POST.get('groups') == 'yes'
        uploaded_file = request.FILES.get('fileUpload')
        subject = request.POST.get('subject')

        # Create instance of your Tutorial class
        tutorial = Tutorial(
            name=name,
            file=uploaded_file,
            file_name = uploaded_file.name,
            type=tutorial_type,
            hint=hint,
            existingGroups=existing_groups,
            subject=subject
        )

        saved_tutorials.append(tutorial)

        # Store the relevant data in session
        request.session['tutorial_data'] = {
            'name': tutorial.name,
            'file_name': tutorial.file_name,
            'type': tutorial.type,
            'hint': tutorial.hint,
            'existingGroups': tutorial.existingGroups,
            'subject': tutorial.subject
        }

        return redirect('success')
    return render(request, 'admin_tutorial.html')

def display_success(request):
    tutorial_data = request.session.get('tutorial_data')
    return render(request, 'success.html', {'tutorial': tutorial_data})