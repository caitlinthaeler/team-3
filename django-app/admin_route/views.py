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
        return redirect('success')
    return redirect('admin_tutorial')