neighborhood_list = list(map(int, input().split('@')))
cupid_position = 0

while True:
    command = input().split()
    if len(command) == 2:
        jump, distance_of_jump = command
    elif len(command) == 1:
        action = command
        if action[0] == 'Love!':
            break

    if int(distance_of_jump) + cupid_position > len(neighborhood_list) - 1:
        cupid_position = 0
    else:
        cupid_position += int(distance_of_jump)

    if neighborhood_list[cupid_position] == 0:
        print(f"Place {cupid_position} already had Valentine's day.")
    else:
        neighborhood_list[cupid_position] -= 2
        if neighborhood_list[cupid_position] == 0:
            print(f"Place {cupid_position} has Valentine's day.")

unloved_houses = [house for house in neighborhood_list if house > 0]

print(f"Cupid's last position was {cupid_position}.")

if len(unloved_houses) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(unloved_houses)} places.")
