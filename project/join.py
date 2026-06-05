# imports and file setup.
import json
import argparse
from pathlib import Path
Task_file = Path.home() /".tasks.json"
# declaration of functions.
def load_tasks():
    if Task_file.exists():
        with open(Task_file, "r") as load_file:
            return json.loads(load_file.read())
        
    return []

def save_tasks():
    with open(Task_file, "r") as save_file:
        save_file.write(json.dumps())

# add task
def add_task(description):
    tasks = load_tasks()
    if len(tasks) == 0:
        next_id = 1
    else:
        next_id = tasks[-1]["id"] + 1

    task = {
        "id": next_id,
        "description": description,
        "completion": False
        }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added tasks #{next_id}: {description}")

def delete_task(task_id):
    tasks = load_tasks()
    result = []
    for loop in tasks():
        if loop["id"] != task_id:
            result.append(loop)
    tasks = result        
    save_tasks(tasks)
    print(f"Deleted id #{task_id}")

def compete_task(task_id):
    tasks = load_tasks()
    for loop in tasks:
        if loop["id"] == task_id:
            loop["completion"] = True
            save_tasks(tasks)
            print(f"Completed task #{task_id}")
            return
    print(f"Task #{task_id} not found")

def update_task(task_id, new_descritpion):
    tasks = load_tasks()
    for loop in tasks:
        if loop["id"] == task_id:
            loop["description"] = new_descritpion
            save_tasks(tasks)
            print(f"Updated task #{task_id}")
            return
    print(f"Task #{task_id} not found")

def search_task(keyword):
    tasks = load_tasks()
    result = []
    for loop in tasks:
        if keyword.lower() in loop["description"].lower():
            result.append(loop)

            if loop["completion"]:
                symbol = "\u2714"
            else:
                symbol = "\u2716"
            print(f"[{symbol}] #{loop["id"]}: {loop["description"]}")

def list_task(show_all=False):
    tasks = load_tasks
    found = False
    for loop in tasks:
        if not show_all and loop["completion"]:
            continue
        found = True    
        if loop["completion"]:
            symbol = "\u2714"
        else:
            symbol = "\u2716"
        print(f"[{symbol}] #{loop["id"]}: {"description"}")
    
    if not found:
        print("No tasks found!")
