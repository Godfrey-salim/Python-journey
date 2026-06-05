import json
# load the json file
with open('fill.json', 'r')as loads_file:
    tasks = json.loads(loads_file.read())
# Prompt to enter task id for completion.
complete_id = int(input("Enter the task id to mark complete: "))
# find and change it(flip).
found = False
for loop in tasks:
    if loop["id"] == complete_id:
        loop["completion"] = True
        found = True
        print(f"The task marked complete: {loop["description"]}")
        break # stop looping, when found.

if not found:
    print(f"Task #{complete_id} not found")

# save
with open('fill.json', 'w') as write_file:
    write_file.write(json.dumps(tasks))
print("Process saved \u2714")
print('Json file updated')