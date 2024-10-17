inventory = input().split(', ')


def collect(user_inventory, user_item):
    if user_item in user_inventory:
        pass
    else:
        user_inventory.append(user_item)

    return user_inventory


def drop(user_inventory, user_item):
    if user_item in user_inventory:
        user_inventory.remove(user_item)
    else:
        pass

    return user_inventory


def combine(user_inventory, user_item1, user_item2):
    if user_item1 in user_inventory:
        old_item_index = user_inventory.index(user_item1)
        user_inventory.insert(old_item_index + 1, user_item2)
    else:
        pass

    return user_inventory


def renew(user_inventory, user_item):
    if user_item in user_inventory:
        user_inventory.remove(user_item)
        user_inventory.append(user_item)

    return user_inventory


while True:
    command = input()
    if command == 'Craft!':
        break
    else:
        command = command.split(' - ')
    action, item = command

    if action == 'Collect':
        inventory = collect(inventory, item)

    elif action == 'Drop':
        inventory = drop(inventory, item)

    elif action == 'Combine Items':
        item = item.split(':')
        item1, item2 = item
        inventory = combine(inventory, item1, item2)
    elif action == 'Renew':
        inventory = renew(inventory, item)

print(', '.join(inventory))
