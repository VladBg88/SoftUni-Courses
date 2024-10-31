groceries_list = input().split('!')


def urgent(user_item, user_list):
    if user_item not in user_list:
        user_list.insert(0, user_item)

    return user_list


def unnecessary(user_item, user_list):
    if user_item in user_list:
        user_list.remove(user_item)

    return user_list


def correct(user_old_item, user_new_item, user_list):
    if user_old_item in user_list:
        old_item_index = user_list.index(user_old_item)
        user_list.pop(old_item_index)
        user_list.insert(old_item_index, user_new_item)

    return user_list


def rearrange(user_item, user_list):
    if user_item in user_list:
        user_list.remove(user_item)
        user_list.append(user_item)

    return user_list


while True:
    command = input().split()

    if len(command) == 1:
        action = command
    elif len(command) == 2:
        action, item = command
    else:
        action, old_item, new_item = command

    if action == 'Go' and item == 'Shopping!':
        break

    if action == 'Urgent':
        groceries_list = urgent(item, groceries_list)
    elif action == 'Unnecessary':
        groceries_list = unnecessary(item, groceries_list)
    elif action == 'Correct':
        groceries_list = correct(old_item, new_item, groceries_list)
    elif action == 'Rearrange':
        groceries_list = rearrange(item, groceries_list)

print(", ".join(groceries_list))
