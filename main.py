import json

filename = "tasks.json"


def add_task(tasks, title):
    task = {
        "title": title,
        "done": False
    }
    tasks.append(task)


def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return

    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "❌"
        print(f"{i}. {task['title']} [{status}]")


def delete_task(tasks):
    view_tasks(tasks)

    num = int(input("Enter task number to delete: "))
    index = num - 1

    del tasks[index]


def mark_done(tasks):
    view_tasks(tasks)

    num = int(input("Enter task number to mark as done: "))
    index = num - 1

    tasks[index]["done"] = True


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1 - Add task")
        print("2 - View tasks")
        print("3 - Exit")
        print("4 - Delete task")
        print("5 - Mark as done")

        choice = input("Choose the action: ")

        if choice == "1":
            title = input("Enter task: ")
            add_task(tasks, title)
            save_tasks(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            print("Bye")
            break

        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)

        elif choice == "5":
            mark_done(tasks)
            save_tasks(tasks)

        else:
            print("Invalid choice!")


main()