number_of_plants = int(input())
all_plants = {}

for plant in range(number_of_plants):
    plant_info = input().split("<->")
    plant_name = plant_info[0]
    plant_rarity = float(plant_info[1])
    all_plants[plant_name] = [plant_rarity]

while True:
    command = input()
    if command == "Exhibition":
        break

    command = command.split()
    if command[0] == "Rate:":
        plant = command[1]
        rating = int(command[3])
        if plant in all_plants:
            all_plants[plant].append(rating)
        else:
            print("error")
    elif command[0] == "Update:":
        plant = command[1]
        new_rarity = int(command[3])
        if plant in all_plants:
            all_plants[plant][0] = new_rarity
        else:
            print("error")
    elif command[0] == "Reset:":
        plant = command[1]
        if plant in all_plants:
            all_plants[plant] = [0]
        else:
            print("error")


print(f"Plants for the exhibition:")
for plant, rarity in all_plants.items():
    if rarity[0] == 0:
        print(f"- {plant}; Rarity: {rarity[0]}; Rating: 0.00")
    else:
        print(f"- {plant}; Rarity: {rarity[0]}; Rating: {sum(rarity[1:]) / len(rarity[1:]):.2f}")