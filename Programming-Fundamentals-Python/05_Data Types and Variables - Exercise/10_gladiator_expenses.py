lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
expenses = 0
shield_broken_counter = 0

for lost_game in range(1, lost_fight_count + 1):
    if lost_game % 2 == 0:
        expenses += helmet_price

    if lost_game % 3 == 0:
        expenses += sword_price

    if lost_game % 3 == 0 and lost_game % 2 == 0:
        expenses += shield_price
        shield_broken_counter += 1

    if shield_broken_counter % 2 == 0 and shield_broken_counter != 0:
        expenses += armour_price
        shield_broken_counter = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')
