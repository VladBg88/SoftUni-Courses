LEFT_BOUNDARY_MUSALA = 1
RIGHT_BOUNDARY_MUSALA = 5
RIGHT_BOUNDARY_MONBLAN = 12
RIGHT_BOUNDARY_KILIMANDZHARO = 25
RIGHT_BOUNDARY_K2 = 40
LEFT_BOUNDARY_EVEREST = 41

number_of_groups = int(input())
total_number_of_people = 0
people_for_musala = 0
people_for_monblan = 0
people_for_kilimandzharo = 0
people_for_k2 = 0
people_for_everest = 0

for _ in range(number_of_groups):
    number_of_people_in_group = int(input())
    total_number_of_people += number_of_people_in_group

    if number_of_people_in_group <= RIGHT_BOUNDARY_MUSALA:
        people_for_musala += number_of_people_in_group
    elif number_of_people_in_group <= RIGHT_BOUNDARY_MONBLAN:
        people_for_monblan += number_of_people_in_group
    elif number_of_people_in_group <= RIGHT_BOUNDARY_KILIMANDZHARO:
        people_for_kilimandzharo += number_of_people_in_group
    elif number_of_people_in_group <= RIGHT_BOUNDARY_K2:
        people_for_k2 += number_of_people_in_group
    else:
        people_for_everest += number_of_people_in_group

print(f"{(people_for_musala / total_number_of_people) * 100:.2f}%")
print(f"{(people_for_monblan / total_number_of_people) * 100:.2f}%")
print(f"{(people_for_kilimandzharo / total_number_of_people) * 100:.2f}%")
print(f"{(people_for_k2 / total_number_of_people) * 100:.2f}%")
print(f"{(people_for_everest / total_number_of_people) * 100:.2f}%")
