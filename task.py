class Task:
    def __init__(self, name, duration, deadline, grade):
        self.name = name
        self.duration = duration
        self.deadline = deadline
        self.grade = grade

    def is_valid(self, T):
        if self.duration < 0 or self.deadline < 0 or self.grade < 0:
            return False
        if self.duration > T:
            return False
        if self.duration > self.deadline:
            return False
        return True
    

