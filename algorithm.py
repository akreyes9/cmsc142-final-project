class Algorithm:
    """
    Deadline-constrained knapsack scheduling using dynamic programming.

    DP State:
    - grade[t]: maximum grade achievable using exactly t hours
    - sequence[t]: ordered task sequence that achieves grade[t]
    """

    def __init__(self, T, tasks):
        self.T = T
        self.tasks = tasks

        self.grade = {}
        self.sequence = {}

    def preprocess(self):
        """
        Sort tasks by deadline (non-decreasing order).
        """
        return sorted(self.tasks, key=lambda task: task.deadline)

    def _initialize_dp(self):
        """
        Initialize DP table.
        """
        self.grade[0] = 0
        self.sequence[0] = []

        for t in range(1, self.T + 1):
            self.grade[t] = float("-inf")
            self.sequence[t] = None

    def _dp_transition(self, tasks):
        """
        Run DP transitions.
        """
        for task in tasks:

            # Backward iteration prevents reusing same task
            for t in range(self.T, -1, -1):

                if self.grade[t] == float("-inf"):
                    continue

                end_time = t + task.duration

                # Feasibility checks
                if end_time > self.T:
                    continue

                if end_time > task.deadline:
                    continue

                new_grade = self.grade[t] + task.grade

                # Keep better solution
                if new_grade > self.grade[end_time]:
                    self.grade[end_time] = new_grade
                    self.sequence[end_time] = (
                        self.sequence[t] + [task]
                    )

    def extract_result(self):
        """
        Extract optimal solution from DP table.

        Returns:
            tuple: (optimal_grade, optimal_sequence)
        """
        best_time = 0
        best_grade = self.grade[0]

        for t in range(self.T + 1):
            if self.grade[t] > best_grade:
                best_grade = self.grade[t]
                best_time = t

        return best_grade, self.sequence[best_time]

    def solve(self):
        """
        Main DP workflow.
        """
        tasks = self.preprocess()

        if not tasks:
            return 0, []

        self._initialize_dp()

        self._dp_transition(tasks)

        return self.extract_result()