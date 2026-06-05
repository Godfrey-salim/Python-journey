import argparse
import json
from pathlib import Path

# Path to the tasks JSON file in user's home directory
Task_file = Path.home() /".tasks.json"

# ===== Storage Operations =====
# Load tasks from file
def load_tasks():
    # Load the task list from the JSON storage file.
    # Returns a list of task dictionaries or an empty list if the file
    # does not exist or is empty.
    if Task_file.exists():
        with open(Task_file, "r") as load_file:
            return json.loads(load_file.read())
    return []


def save_tasks(tasks):
    # Persist the provided list of tasks to the JSON storage file.
    # Overwrites any existing data.
    with open(Task_file, "w") as save_file:
        save_file.write(json.dumps(tasks))

# Project operations

def add_tasks(description):
    # Add a new task with an auto-incremented ID and default completion state.
    tasks = load_tasks()
    if len(tasks) ==0:
        next_id = 1
    else:
        next_id = tasks[-1]["id"]+ 1
    
    task = {
        "id": next_id,
        "description": description,
        "completion": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{next_id}: {description}")

def delete_tasks(task_id):
    # Remove the task with the given ID from storage.
    tasks = load_tasks()
    tasks = [loop for loop in tasks if loop["id"] != task_id]
    save_tasks(tasks)
    print(f"Deleted task #{task_id}")

def complete_task(task_id):
    # Mark the task with the specified ID as completed.
    tasks = load_tasks()
    for loop in tasks:
        if loop["id"] == task_id:
            loop["completion"] = True
            save_tasks(tasks)
            print(f"Completed task #{task_id}")
            return
    print(f"Task #{task_id} not found")

def update_task(task_id, new_description):
    # Update the description for a specific task ID.
    tasks = load_tasks()
    for loop in tasks:
        if loop["id"]== task_id:
            loop["description"] = new_description
            save_tasks(tasks)
            print(f"Task #{task_id} updated to {new_description}")
            return
    print(f"Task #{task_id} not found")

def search_tasks(keyword):
    # Search tasks for a keyword in the description and print matches.
    tasks= load_tasks()
    found = False
    for loop in tasks:
        if keyword.lower() in loop["description"].lower():
            found = True
            if loop["completion"]:
                symbol = "\u2714"
            else:
                symbol = "\u2716"
            print(f"[{symbol}] #{loop['id']}: {loop['description']}")
    
    if not found:
        print(f"No matching tasks")

def list_tasks(show_all=False):
    # List tasks to the console. By default only shows incomplete tasks;
    # set show_all=True to include completed tasks.
    tasks = load_tasks()
    if not show_all:
        tasks = [loop for loop in tasks if not loop["completion"]]
    if not tasks:
        print("no tasks")
    for loop in tasks:
        if loop["completion"]:
            symbol = "\u2714"
        else:
            symbol = "\u2716"
        print(f"[{symbol}] #{loop['id']}: {loop['description']}")

# command line interface.
# while adding,searching and updating tasks, put double quotes around the description if it contains spaces. For example:"buy milk" instead of buy milk.

def main():
    parser = argparse.ArgumentParser(description="Personal Task CLI Manager")
    subparsers = parser.add_subparsers(dest="command")
    
    # list 
    subparsers.add_parser("list", help="list incomplete tasks")
    subparsers.add_parser("list-all", help="list all tasks including completed")
     
     # add
    p = subparsers.add_parser("add", help="add a new task")
    p.add_argument("description", type=str, help="Task description")

    # delete
    p = subparsers.add_parser("delete", help="Delete a task")
    p.add_argument("id", type=int, help="Task ID to delete")

    # completion
    p = subparsers.add_parser("complete", help="Mark a task complete")
    p.add_argument("id", type=int, help="Task ID to complete")

    # search
    p = subparsers.add_parser("search", help="Search task by keyword")
    p.add_argument("keyword", type=str, help="keyword to search for")

    # update 
    p = subparsers.add_parser("update",help="Update a task description")
    p.add_argument("id", type=int, help="Task id to update")
    p.add_argument("description", type=str, help="New description")

    args = parser.parse_args()

    # route command to the right function
    if args.command == "add":
        add_tasks(args.description)
    elif args.command == "delete":
        delete_tasks(args.id)
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "update":
        update_task(args.id, args.description)
    elif args.command == "search":
        search_tasks(args.keyword)
    elif args.command == "list":
        list_tasks()
    elif args.command == "list-all":
        list_tasks(show_all=True)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


