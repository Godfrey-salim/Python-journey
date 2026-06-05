import json


workdone = str(input("Enter task to be done: "))
description = str(input("Enter the descripton of your task: "))

new_tasks = {
    "info": workdone, "completion": False, "item": "groceries"
}
tasks= [
    {"info": workdone, "completion": False, "item": "buy milk"},
    {"info": description, "completion": True, "item": "potatoes"}
]

tasks.append(new_tasks)

string_text = json.dumps(tasks)

with open('workdone.json', 'w') as write_file:
    write_file.write(string_text)

with open('workdone.json', 'r') as load_file:
    content = load_file.read()
info = json.loads(content)

for number, loop in enumerate (info):
    if loop["completion"]:
        symbol = '\u2714'
    else:
        symbol = '\u2716'
    print(f'{number}. [{symbol}]: Completion of task -- {loop["item"]}')
