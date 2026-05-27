def build_schedule(sequence):
    """
    Convert task sequence into wall-clock schedule.
    """

    schedule = []

    current_time = 0

    for task in sequence:

        start_time = current_time
        end_time = current_time + task.duration

        schedule.append({
            "task": task,
            "start": start_time,
            "end": end_time
        })

        current_time = end_time

    return schedule


def display_results(optimal_grade, optimal_sequence):
    """
    Display final scheduling results.
    """

    print("\n" + "=" * 60)
    print("OPTIMAL SCHEDULE")
    print("=" * 60)

    print(f"\nMaximum Achievable Grade: {optimal_grade}")

    if not optimal_sequence:
        print("\nNo feasible schedule found.")
        return

    schedule = build_schedule(optimal_sequence)

    print(f"\nTask Execution Plan ({len(schedule)} tasks):\n")

    for i, slot in enumerate(schedule, 1):

        task = slot["task"]

        print(f"{i}. {task.name}")

        print(
            f"   Time: "
            f"{slot['start']}h - {slot['end']}h"
        )

        print(f"   Estimated time for completion (hours): {task.duration} hours")

        print(f"   Grade Contribution: +{task.grade}")

        print()

    total_time = schedule[-1]["end"]

    print(f"Total Study Time Used: {total_time} hours")

    print("=" * 60 + "\n")