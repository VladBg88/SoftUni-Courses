def register(username: str, license_plate_number: int):
    if name not in database:
        database[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")
    else:
        print(f"ERROR: already registered with plate number {database[name]}")
    return database


def unregister(username):
    if username in database:
        print(f"{username} unregistered successfully")
        del database[username]
    else:
        print(f"ERROR: user {username} not found")
    return database


number_of_commands = int(input())
database = {}

for i in range(number_of_commands):
    command = input().split()
    if len(command) == 3:
        action, name, license_plate = command[0], command[1], command[2]
    elif len(command) == 2:
        action, name = command[0], command[1]

    if action == 'register':
        database = register(name, license_plate)
    elif action == 'unregister':
        database = unregister(name)

for name, license_plate in database.items():
    print(f"{name} => {license_plate}")
