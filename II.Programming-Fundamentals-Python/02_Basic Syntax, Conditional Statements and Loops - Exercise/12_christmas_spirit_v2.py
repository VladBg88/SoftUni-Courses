quantity = int(input())
days = int(input())

prices = {
    "Ornament Set": 2,
    "Tree Skirt": 5,
    "Tree Garland": 3,
    "Tree Lights": 15
}

points = {
    "Ornament Set": 5,
    "Tree Skirt": 3,
    "Tree Garland": 10,
    "Tree Lights": 17
}

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += prices["Ornament Set"] * quantity
        total_spirit += points["Ornament Set"]

    if day % 3 == 0:
        total_cost += prices["Tree Skirt"] * quantity
        total_spirit += points["Tree Skirt"]
        total_cost += prices["Tree Garland"] * quantity
        total_spirit += points["Tree Garland"]

    if day % 5 == 0:
        total_cost += prices["Tree Lights"] * quantity
        total_spirit += points["Tree Lights"]
        if day % 3 == 0:
            total_spirit += 30

    if day % 10 == 0:
        total_spirit -= 20
        total_cost += prices["Tree Skirt"]
        total_cost += prices["Tree Garland"]
        total_cost += prices["Tree Lights"]

    if day == days and day % 10 == 0:
        total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")