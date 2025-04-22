forces = {}


while True:
    action_one = False
    action_two = False

    command = input()

    if command == 'Lumpawaroo':
        break
    if '|' in command:
        command = command.split(' | ')
        force_side, force_user = command
        action_one = True
    elif '->' in command:
        command = command.split(' -> ')
        force_user, force_side = command
        action_two = True

    if action_one:
        if force_side not in forces:
            forces[force_side] = []
        if not any(force_user in users for users in forces.values()):
            forces[force_side] += [force_user]
    elif action_two:
        for side, user in forces.items():
            if force_user in user:
                user.remove(force_user)
                break

        if force_side not in forces:
            forces[force_side] = []
        forces[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for sides, users in forces.items():
    if users:
        print(f"Side: {sides}, Members: {len(users)}")
        for element in users:
            print(f"! {element}")
