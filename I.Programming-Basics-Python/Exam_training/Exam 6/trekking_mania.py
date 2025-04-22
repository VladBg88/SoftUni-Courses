number_of_groups = int(input())
musala_count = 0
monblan_count = 0
kilimandzaro_count = 0
k2_count = 0
everest_count = 0

for i in range(number_of_groups):
    people = int(input())

    if people <= 5:
        musala_count += people
    elif people <= 12:
        monblan_count += people
    elif people <= 25:
        kilimandzaro_count += people
    elif people <= 40:
        k2_count += people
    else:
        everest_count += people

total_people = musala_count + monblan_count + kilimandzaro_count + k2_count + everest_count

print(f'{100 / total_people * musala_count:.2f}%')
print(f'{100 / total_people * monblan_count:.2f}%')
print(f'{100 / total_people * kilimandzaro_count:.2f}%')
print(f'{100 / total_people * k2_count:.2f}%')
print(f'{100 / total_people * everest_count:.2f}%')
