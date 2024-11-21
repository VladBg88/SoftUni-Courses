import re

demon_names = input().split(',')
pattern_health = r"[^0-9\.\+\-\*\/]"
pattern_numbers = r"[-|+]?[0-9]+\.[0-9]+|[+|-]?[0-9]+"
demon_dict = {}
alphabet_sorted = {}
demon_names = [demon.strip() for demon in demon_names]

for demon in demon_names:
    health_bars = re.findall(pattern_health, demon)
    health = sum(ord(letter) for letter in health_bars)

    damage_bars = re.findall(pattern_numbers, demon)
    damage = sum(float(number) for number in damage_bars)

    for symbol in demon:
        if symbol == '*':
            damage *= 2
        elif symbol == '/':
            damage /= 2

    if demon not in demon_dict:
        demon_dict[demon] = []
    demon_dict[demon].append(health)
    demon_dict[demon].append(damage)

    alphabet_sorted = dict(sorted(demon_dict.items()))

for name, stat in alphabet_sorted.items():
    print(f"{name} - {demon_dict[name][0]} health, {demon_dict[name][1]:.2f} damage")