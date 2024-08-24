import sys

def remove_task(index, tasks):
    try:
        removed_task= tasks.pop(index - 1)
        print(f'Removed task: "{removed_task}"')
        save_tasks(tasks)
    except IndexError:
        print("Error: Invalid task number.")

def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
             tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
         for task in tasks:
             file.write(task + "\n")


def add_task(task, tasks):
    tasks.append(task)
    print("Added task: "+task)
    save_tasks(tasks)

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the List.")
    else:
        print("Todo List: ")
        for i, task in enumerate(tasks, 1):
           print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "add":
            task = " ".join(sys.argv[2:])
            add_task(task,tasks)
        elif command == "list":
            list_tasks(tasks)
        elif command == "remove":
             try:
                 index = int(sys.argv[2])
                 remove_task(index, tasks)
             except (IndexError, ValueError):
                 print("Error: Please provide a valid task number.")
        else: 
             print("Unnown command")
    else: 
         print("Todo List Application")
         print("Usage: todo.py add <task>")
         print("       todo.py list")

if __name__ == "__main__":
    main()
