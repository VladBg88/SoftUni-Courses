days_of_adventure = int(input())
participants_number = int(input())
energy_of_group = float(input())
water_per_person_day = float(input())
food_per_person_day = float(input())

total_water_needed = round((water_per_person_day * participants_number) * days_of_adventure, 2)
total_food_needed = round((food_per_person_day * participants_number) * days_of_adventure, 2)

for day in range(1, days_of_adventure + 1):
    chop_chop = float(input())
    energy_of_group -= chop_chop
    if energy_of_group <= 0:
        print(f"You will run out of energy. You will be left with {total_food_needed:.2f} food and {total_water_needed:.2f} water.")
        break

    if day % 2 == 0:
        energy_of_group = round(energy_of_group * 1.05, 2)
        total_water_needed = round(total_water_needed * 0.70, 2)

    if day % 3 == 0:
        energy_of_group = round(energy_of_group * 1.10, 2)
        total_food_needed -= round(total_food_needed / participants_number, 2)

    if day == days_of_adventure:
        print(f"You are ready for the quest. You will be left with {energy_of_group:.2f} energy!")