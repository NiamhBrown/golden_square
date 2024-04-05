class Reminder:

    def __init__(self, name, task=None):
        self.name = name 
        self.task = task

    def remind_me_to(self, task):
        self.task = task

    def remind(self):
        if self.task is None:
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"