number_of_heroes = int(input())
all_heroes = {}

for hero in range(number_of_heroes):
    hero_name, hero_health, hero_mana = map(str, input().split())
    all_heroes[hero_name] = {"health": int(hero_health), "mana": int(hero_mana)}

while True:
    command = input().split(' - ')
    if command[0] == "End":
        for hero_name, hero_info in all_heroes.items():
            print(f"{hero_name}\n"
                  f"  HP: {hero_info['health']}\n"
                  f"  MP: {hero_info['mana']}")
        break
    elif command[0] == "CastSpell":
        hero_name, mana_cost, spell_name = command[1], int(command[2]), command[3]
        if all_heroes[hero_name]["mana"] >= mana_cost:
            all_heroes[hero_name]["mana"] -= mana_cost
            print(f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        hero_name, damage, attacker = command[1], int(command[2]), command[3]
        all_heroes[hero_name]["health"] -= damage
        if all_heroes[hero_name]["health"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {all_heroes[hero_name]['health']} HP left!")
        else:
            del all_heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        hero_name, amount = command[1], int(command[2])
        recharged = min(amount, 200 - all_heroes[hero_name]["mana"])
        all_heroes[hero_name]["mana"] += amount
        if all_heroes[hero_name]["mana"] > 200:
            all_heroes[hero_name]["mana"] = 200
        print(f"{hero_name} recharged for {recharged} MP!")
    elif command[0] == "Heal":
        hero_name, amount = command[1], int(command[2])
        healed = min(amount, 100 - all_heroes[hero_name]["health"])
        all_heroes[hero_name]["health"] += amount
        if all_heroes[hero_name]["health"] > 100:
            all_heroes[hero_name]["health"] = 100
        print(f"{hero_name} healed for {healed} HP!")
