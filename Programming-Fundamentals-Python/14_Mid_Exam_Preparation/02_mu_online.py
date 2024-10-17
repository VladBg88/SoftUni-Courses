initial_health = 100
initial_bitcoins = 0
dungeon_rooms = input().split('|')
died = False


def potion(user_health, user_points):
    healed = min(user_points, 100 - user_health)
    user_health += healed
    print(f'You healed for {healed} hp.')
    print(f'Current health: {user_health} hp.')
    return user_health


def chest(bitcoins, user_points):
    bitcoins += user_points
    print(f'You found {user_points} bitcoins.')
    return bitcoins


def monster(user_health, user_found, user_points):
    user_health -= user_points
    if user_health <= 0:
        print(f'You died! Killed by {user_found}.')
        return 0
    else:
        print(f'You slayed {user_found}.')
    return user_health


for room in range(len(dungeon_rooms)):
    inside_room = dungeon_rooms[room].split()
    event_type, value = inside_room[0], int(inside_room[1])

    if event_type == 'potion':
        initial_health = potion(initial_health, value)
    elif event_type == 'chest':
        initial_bitcoins = chest(initial_bitcoins, value)
    else:
        initial_health = monster(initial_health, event_type, value)
        if initial_health <= 0:
            print(f"Best room: {room + 1}")
            died = True
            break


if not died:
    print("You've made it!")
    print(f"Bitcoins: {initial_bitcoins}")
    print(f"Health: {initial_health}")
