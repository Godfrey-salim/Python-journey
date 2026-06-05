import json
#importing an extension of json with the name "fill.json".
with open('fill.json', 'r') as read_file:
   reading = read_file.read()
pis = json.loads(reading)
print(pis)
# enumerate helps to display the index of the item.
for number, loop in enumerate(pis):
    if loop["completion"]:
      symbol = "\u2714"
    else:
       symbol = "\u2716"
    print(f"{number}. [{symbol}] {loop['description']}")