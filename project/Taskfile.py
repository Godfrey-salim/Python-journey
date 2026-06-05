import json
tasks = [
    {"id": 1, "description": "Buy milk", "completion": False}
]
new_task ={
    "id": 2,
    "description": "Go to the market", "completion": True
    }
# joining of the dictinary and a list.
tasks.append(new_task)

info = json.dumps(tasks)

with open('fill.json', 'w')as writing:
    writing.write(info)

print('File saved')

with open('fill.json', 'r') as reading:
    read_file = reading.read()
    pass
python90 = json.loads(read_file)
print('file is okay')
print(python90[1])
for loop in tasks:
    Description = loop['description']
    completion = loop ['completion']
    print(f'Task: {Description} | done: {completion}')