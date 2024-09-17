group_size = int(input())
days_of_adventure = int(input())
money = 0

for days in range(1, days_of_adventure + 1):
    if days % 10 == 0:
        group_size -= 2

    if days % 15 == 0:
        group_size += 5

    money += 50  # everyday earning
    money -= 2 * group_size  # group consumption

    if days % 3 == 0:
        money -= 3 * group_size  # motivational party

    if days % 5 == 0:
        money += 20 * group_size
        if days % 3 == 0:
            money -= 2 * group_size

print(f'{group_size} companions received {money // group_size} coins each.')
