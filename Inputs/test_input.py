from input_handling import InputHandler

handler = InputHandler()

T, tasks = handler.get_input()

print("\n\n===== Data Passed to DP Module =====")
print("Total Time T:", T)

handler.print_tasks(tasks)