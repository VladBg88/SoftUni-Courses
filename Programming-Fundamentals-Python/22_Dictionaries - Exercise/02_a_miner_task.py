database = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in database:
        database[resource] = 0
    database[resource] += quantity

for resource, quantity in database.items():
    print(f"{resource} -> {quantity}")
