from task import Task

class InputHandler:

    # Input Guard
    def safe_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    # Input Functions
    def get_input(self):
        choice = input("Select input mode (1 = Manual Entry, 2 = CSV Import): ")

        if choice == "2":
            filename = input("Enter CSV filename (e.g., tasks.csv): ")
            tasks = self.load_from_csv(filename)

            T = self.safe_int("Enter available study time (hours): ")
            tasks = self.validate_tasks(T, tasks)

            return T, tasks

        else:
            T = self.safe_int("Enter available study time (hours): ")
            n = self.safe_int("Enter number of tasks: ")

            tasks = []

            for i in range(n):
                print(f"\n----- Task {i + 1} -----")

                name = input("Enter task name: ")

                duration = self.safe_int(
                    "Estimated time for completion (hours): "
                )

                deadline = self.safe_int(
                    "Deadline (hours until due): "
                )

                grade = self.safe_int(
                    "Grade contribution: "
                )

                tasks.append(Task(name, duration, deadline, grade))

            tasks = self.validate_tasks(T, tasks)

            return T, tasks

    # VALIDATION
    def validate_tasks(self, T, tasks):
        valid = []

        for task in tasks:
            if task.is_valid(T):
                valid.append(task)
            else:
                print(f"Skipping invalid task: {task.name}")

        return valid

    # CSV LOADING
    def load_from_csv(self, filename):
        tasks = []

        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print("File not found.")
            return []

        lines = file.readlines()
        file.close()

        if len(lines) == 0:
            return []

        start_index = 0
        if "name" in lines[0].lower():
            start_index = 1

        for i in range(start_index, len(lines)):
            line = lines[i].strip()

            if line == "":
                continue

            parts = line.split(",")

            if len(parts) != 4:
                print(f"Skipping malformed row: {line}")
                continue

            name = parts[0]

            try:
                duration = int(parts[1])
                deadline = int(parts[2])
                grade = int(parts[3])
            except ValueError:
                print(f"Skipping invalid row: {line}")
                continue

            tasks.append(Task(name, duration, deadline, grade))

        return tasks

    # Output Format
    def print_tasks(self, tasks):
        print("\n===== VALID TASKS =====\n")

        for task in tasks:
            print(
                f"Name: {task.name} | "
                f"Duration: {task.duration} hours | "
                f"Deadline: {task.deadline} hours | "
                f"Grade: {task.grade}"
            )