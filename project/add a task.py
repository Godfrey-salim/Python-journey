import json

with open('fill.json', 'r') as load_file:
    content = load_file.read()
tasks =json.loads(content)

if len(tasks) == 0:
    next_id = 1
else:
    last_task = tasks[-1]          
    next_id = last_task["id"] + 1  

info = input("Enter task: ")
new_task = {
    "id": next_id,
    "description": info,
    "completion": False
}

tasks.append(new_task)
text = json.dumps(tasks)

with open('fill.json', 'w') as write_file:
    write_file.write(text)

for loop in tasks:
    if loop["completion"]:
        symbol = "\u2714"
    else:
        symbol = "\u2716"

    print(f'{symbol}. {loop["id"]}: {loop["description"]}')