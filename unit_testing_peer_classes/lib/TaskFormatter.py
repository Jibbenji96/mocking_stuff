class TaskFormatter:
    def __init__(self, task): # task is an instance of Task
        self.task = task

    def format(self):
        if self.task.complete == True:
            return f"- [x] {self.task.name}"
        else:
            return f"- [ ] {self.task.name}"
