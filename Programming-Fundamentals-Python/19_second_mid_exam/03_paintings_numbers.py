paintings = input().split()

while True:
    command = input().split()
    if command[0] == 'END':
        break

    action = command[0]

    if action == 'Change':
        if command[1] in paintings:
            index_work_on = paintings.index(command[1])
            paintings[index_work_on] = command[2]
    elif action == 'Hide':
        if command[1] in paintings:
            paintings.remove(command[1])
    elif action == 'Switch':
        if command[1] in paintings and command[2] in paintings:
            index_1 = paintings.index(command[1])
            index_2 = paintings.index(command[2])
            paintings[index_1], paintings[index_2] = paintings[index_2], paintings[index_1]
    elif action == "Insert":
        if 0 <= int(command[1]) <= len(paintings):
            paintings.insert(int(command[1]) + 1, command[2])
    elif action == "Reverse":
        paintings.reverse()

print(*paintings)
