class Algorithm:
    def __init__(self, T, tasks):
        self.T = T
        self.tasks = tasks
        self.grade = {}
        self.best_grade = 0     
        self.best_time = 0 

    def sort_tasks(self):
        return sorted(self.tasks, key=lambda task: task.deadline)

    def initialize_dp(self):
        """Initialize DP table."""
        self.grade[0] = 0
        for t in range(1, self.T + 1):
            self.grade[t] = float("-inf")

    def dp_transition(self, tasks):
        for task in tasks:
            for t in range(self.T, -1, -1):
                if self.grade[t] == float("-inf"):
                    continue
                
                end_time = t + task.duration
                
                if end_time > self.T or end_time > task.deadline:
                    continue
                
                new_grade = self.grade[t] + task.grade
                
                if new_grade > self.grade[end_time]:
                    self.grade[end_time] = new_grade
                    
                    # Update best grade on the fly
                    if new_grade > self.best_grade:
                        self.best_grade = new_grade
                        self.best_time = end_time

    def extract_result(self, tasks):
        """Extract optimal time and backtrack to find selected tasks."""
        selected = []
        current_time = self.best_time
        
        for task in reversed(tasks):
            prev_time = current_time - task.duration
            
            # Safety check: if we'd go negative, this task wasn't used
            if prev_time < 0:
                continue
                
            if self.grade[prev_time] != float("-inf") and \
            self.grade[current_time] - self.grade[prev_time] == task.grade:
                selected.append(task)
                current_time = prev_time
        
        return self.best_grade, list(reversed(selected))

    def solve(self):
        """Main DP workflow."""
        tasks = self.sort_tasks()
        
        if not tasks:
            return 0, []
        
        self.initialize_dp()
        self.dp_transition(tasks)
        
        return self.extract_result(tasks)