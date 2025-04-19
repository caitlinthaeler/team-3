class Tutorial:
    def _init_(self, name, file, type, hint = None, existingGroups=False):
        self.name = name
        self.file = file
        self.type = type
        self.existingGroups = existingGroups
        self.hint = hint
        self.submissions = []

    def add_submission(self, submission):
        self.submissions.append(submission)