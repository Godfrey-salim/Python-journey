import json

with open('fill.json', 'r') as loads_file:
    content = loads_file.read()
tasks = json.loads(content)

remove_task =int(input("Enter the id number of item you want removed or deleted: "))
remaining_task = []

for loop in tasks:
    if loop["id"] != remove_task:
        remaining_task.append(loop)

print(f'The remaining tasks : {remaining_task}')


with open('fill.json', 'w') as new_file:
    new_file.write(json.dumps(remaining_task))
    pass
print('file has been updated')
print(f"The resulting tasks: ", remaining_task)