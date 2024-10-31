waiting_people = int(input())
lift_wagons = list(map(int, input().split()))
empty_spaces = False

for i in range(len(lift_wagons)):
    free_space = 4 - lift_wagons[i]

    if waiting_people >= free_space:
        lift_wagons[i] += free_space
        waiting_people -= free_space
    else:
        lift_wagons[i] += waiting_people
        waiting_people = 0

    if waiting_people == 0:
        break

if any(wagon < 4 for wagon in lift_wagons):
    print("The lift has empty spots!")
    print(*lift_wagons)
elif waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
    print(*lift_wagons)
else:
    print(*lift_wagons)
