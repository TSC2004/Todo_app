import json
import os

filename = "tasks.json"

def load():
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return []

def save(tasks):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)

def show(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks):
        done = "Done" if t["done"] else "-"
        print(f"{i+1}. {t['title']} | {t['priority']} | {t['due']} | {done}")

def add(tasks):
    title = input("Task: ")
    priority = input("Priority (High/Medium/Low): ")
    due = input("Due date (DD-MM-YYYY): ")
    task = {"title": title, "priority": priority, "due": due, "done": False}
    tasks.append(task)
    print("Task added.")

def edit(tasks):
    show(tasks)
    i = int(input("Task no. to edit: ")) - 1
    if 0 <= i < len(tasks):
        t = tasks[i]
        t["title"] = input(f"New title ({t['title']}): ") or t["title"]
        t["priority"] = input(f"New priority ({t['priority']}): ") or t["priority"]
        t["due"] = input(f"New due date ({t['due']}): ") or t["due"]
        print("Task updated.")
    else:
        print("Invalid number.")

def delete(tasks):
    show(tasks)
    i = int(input("Task no. to delete: ")) - 1
    if 0 <= i < len(tasks):
        tasks.pop(i)
        print("Task deleted.")
    else:
        print("Invalid number.")

def done(tasks):
    show(tasks)
    i = int(input("Task no. to mark done: ")) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        print("Marked as done.")
    else:
        print("Invalid number.")

def main():
    tasks = load()
    while True:
        print("\n1. Show\n2. Add\n3. Edit\n4. Delete\n5. Done\n6. Save\n7. Exit")
        ch = input("Choice: ")
        if ch == "1":
            show(tasks)
        elif ch == "2":
            add(tasks)
        elif ch == "3":
            edit(tasks)
        elif ch == "4":
            delete(tasks)
        elif ch == "5":
            done(tasks)
        elif ch == "6":
            save(tasks)
            print("Saved.")
        elif ch == "7":
            save(tasks)
            print("!!Thankyou!!")
            break
        else:
            print("Invalid choice.")

main()
