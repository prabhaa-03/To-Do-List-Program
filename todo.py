tasks = []

def add_task(task):
    tasks.append({"task" : task, "done" : False})

def mark_done(task_index):
    if 0<= task_index < len(tasks):
        tasks[task_index] ["done"] = True
    else:
        print("Invalid task index")

def delete_task(task_index):
    if 0<= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Invalid task index")

def show_tasks():
    for i, task in enumerate(tasks):
        if task['done']:
            print(f"{i}. {task['task']} - Done")
        else:
            print(f"{i}. {task['task']} - Not Done")

def main():
    while True:
        print("\\nTo-Do List Application")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Exit")

        choice = input("Enter your choice : ")

        if choice == "1":
            task = input("Enter your task : ")
            add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to mark as done : "))
            mark_done(task_index)
        elif choice == "3":
            task_index = int(input("Enter task index to delete : "))
            delete_task(task_index)
        elif choice == "4":
            show_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")


main()