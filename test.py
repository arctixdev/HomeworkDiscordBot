import json

with open("commands.json", "r") as f:
    data = json.loads(f.read())

print(data)


class command:
    name = ""
    description = ""

commands = {}

for i in data:
    commands[i] = command()
    commands[i].name = i
    print(i)
    for y in data[i]:
        commands[i].description = data[i][y]

print(commands["update"].description)
