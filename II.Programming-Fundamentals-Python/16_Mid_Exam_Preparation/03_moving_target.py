moving_targets_list = list(map(int, input().split()))


def shoot(user_list, user_index, user_value):
    if 0 <= user_index < len(user_list):
        user_list[user_index] -= user_value
        if user_list[user_index] <= 0:
            user_list.pop(user_index)

    return user_list


def add(user_list, user_index, user_value):
    if 0 <= user_index < len(user_list):
        user_list.insert(user_index, user_value)
    else:
        print("Invalid placement!")

    return user_list


def strike(user_list, user_index, user_value):
    if user_index + user_value < len(user_list) and user_index - user_value >= 0:
        min_index = user_index - user_value
        max_index = user_index + user_value
        for i in range(max_index, min_index - 1, -1):
            user_list.pop(i)
    else:
        print("Strike missed!")

    return user_list


while True:
    command = input()
    if command == 'End':
        break
    else:
        command = command.split()
        index, value = int(command[1]), int(command[2])

    if 'Shoot' in command:
        moving_targets_list = shoot(moving_targets_list, index, value)
    elif 'Add' in command:
        moving_targets_list = add(moving_targets_list, index, value)
    elif 'Strike' in command:
        moving_targets_list = strike(moving_targets_list, index, value)

print("|".join(map(str, moving_targets_list)))
