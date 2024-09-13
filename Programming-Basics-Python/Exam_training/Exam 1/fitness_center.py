number_of_people = int(input())
back_counter = 0
chest_counter = 0
legs_counter = 0
abs_counter = 0
protein_shake_counter = 0
protein_bar_counter = 0

for _ in range(number_of_people):
    action = str(input())
    if action == "Back":
        back_counter += 1
    elif action == "Chest":
        chest_counter += 1
    elif action == "Legs":
        legs_counter += 1
    elif action == "Abs":
        abs_counter += 1
    elif action == "Protein shake":
        protein_shake_counter += 1
    elif action == "Protein bar":
        protein_bar_counter += 1

percent = 100 / number_of_people
work_out = back_counter + chest_counter + legs_counter + abs_counter
protein = protein_bar_counter + protein_shake_counter

print(f"{back_counter} - back")
print(f"{chest_counter} - chest")
print(f"{legs_counter} - legs")
print(f"{abs_counter} - abs")
print(f"{protein_shake_counter} - protein shake")
print(f"{protein_bar_counter} - protein bar")
print(f"{work_out * percent:.2f}% - work out")
print(f"{protein * percent:.2f}% - protein")
