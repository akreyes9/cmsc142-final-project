from input_handler import InputHandler
from algorithm import Algorithm
from output_handler import display_results

def print_header():
    print("=" * 70)
    print("        STUDENT TASK SCHEDULING SYSTEM")
    print("=" * 70)

    print("\nThis system helps students maximize their grade")
    print("within a limited amount of study time using optimal scheduling.\n")

    print("Rules:")

    print("- Tasks must finish before their deadline")
    print("- Each task has an estimated completion time")
    print("- Grade represents contribution to final grade")
    print("- No negative time and deadline")
    print("- Available time is from your chosen start time until the latest task deadline")
    print("- Task names should be unique for clearer outputs\n")

    print("Invalid Cases:")
    print("- Deadline is earlier than the estimated completion time")
    print("- Estimated completion time exceeds the available study time\n")

    print("=" * 70)


def main():

    print_header()

    input_handler = InputHandler()

    T, tasks = input_handler.get_input()

    input_handler.print_tasks(tasks)

    algorithm = Algorithm(T, tasks)

    optimal_grade, optimal_sequence = algorithm.solve()

    display_results(optimal_grade, optimal_sequence)


if __name__ == "__main__":
    main()