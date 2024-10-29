target = list(map(int, input().split('|')))
total_points = 0

while True:
    command = input()
    if command == "Game over":
        break

    indices = command.split("@")
    action = indices[0]

    if action == "Shoot Left":
        start_index, length = int(indices[1]), int(indices[2])
        if 0 <= start_index < len(target):

            target_index = (start_index - length) % len(target)
            if target[target_index] < 5:
                total_points += target[target_index]
                target[target_index] = 0
            else:
                total_points += 5
                target[target_index] -= 5
    elif action == "Shoot Right":
        start_index, length = int(indices[1]), int(indices[2])
        if 0 <= start_index < len(target):
            target_index = (start_index + length) % len(target)
            if target[target_index] < 5:
                total_points += target[target_index]
                target[target_index] = 0
            else:
                total_points += 5
                target[target_index] -= 5
    elif action == "Reverse":
        target.reverse()

field_output = " - ".join(map(str, target))
print(f"{field_output}")
print(f"John finished the archery tournament with {total_points} points!")
