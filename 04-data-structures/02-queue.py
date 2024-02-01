from queue import Queue

to_do_list = Queue()

to_do_list.put("Task 1")
to_do_list.put("Task 2")
to_do_list.put("Task 3")

while not to_do_list.empty():
    current_task = to_do_list.get()
    print("Working on:", current_task)
    print("Completed:", current_task)

print("All tasks completed.")
