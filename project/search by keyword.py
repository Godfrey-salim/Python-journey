import json
# loads the json extension file.
with open('fill.json', 'r') as load_file:
    tasks = json.loads(load_file.read())
# Search prompt.
keyword = input("Search for: ")

found = False
for loop in tasks:
    if keyword.lower() in loop['description'].lower():
        found = True
        if loop["completion"]:
            symbol = "\u2714"
        else:
            symbol = "\u2716"
        print(f"[{symbol}] #{loop["id"]} {loop["description"]}")

if not found:
    print("no matching tasks")