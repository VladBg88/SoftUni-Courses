ORNAMENT_SET_PRICE = 2
ORNAMENT_SET_POINTS = 5
TREE_SKIRT_PRICE = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_PRICE = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_PRICE = 15
TREE_LIGHTS_POINTS = 17

quantity_of_decorations = int(input())
days_left = int(input())
budget = 0
totalSpirit = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2

    if day % 2 == 0:
        budget += ORNAMENT_SET_PRICE * quantity_of_decorations
        totalSpirit += ORNAMENT_SET_POINTS

    if day % 3 == 0:
        budget += TREE_SKIRT_PRICE * quantity_of_decorations
        budget += TREE_GARLAND_PRICE * quantity_of_decorations
        totalSpirit += TREE_SKIRT_POINTS + TREE_GARLAND_POINTS

    if day % 5 == 0:
        budget += TREE_LIGHTS_PRICE * quantity_of_decorations
        totalSpirit += TREE_LIGHTS_POINTS

    if day % 5 == 0 and day % 3 == 0:
        totalSpirit += 30

    if day % 10 == 0:
        totalSpirit -= 20
        budget += TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE

#    if day == days_left and day % 10 == 0:
#        totalSpirit -= 30

 #   if day % 11 == 0:
 #       quantity_of_decorations -= 2

print(f"Total cost: {budget}")
print(f"Total spirit: {totalSpirit}")
