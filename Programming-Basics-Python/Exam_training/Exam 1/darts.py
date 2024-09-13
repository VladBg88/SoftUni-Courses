TARGET = 301
SINGLE = 1
DOUBLE = 2
TRIPLE = 3

player_name = str(input())
successful_shots_count = 0
unsuccessful_shots_count = 0

while True:
    field = str(input())
    if field == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots_count} unsuccessful shots.")
        break
    points = int(input())

    if field == "Single":
        points = points * SINGLE
    elif field == "Double":
        points = points * DOUBLE
    elif field == "Triple":
        points = points * TRIPLE

    if points > TARGET:
        unsuccessful_shots_count += 1
        continue

    successful_shots_count += 1
    TARGET -= points

    if TARGET == 0:
        print(f"{player_name} won the leg with {successful_shots_count} shots.")
        break
