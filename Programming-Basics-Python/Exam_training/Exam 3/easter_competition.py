bakes = int(input())
best_points = 0
best_man = ""
sum_points = 0

while True:
    if bakes == 0:
        print(f'{best_man} won competition with {best_points} points!')
        break
    name_of_baker = str(input())
    while True:
        command = input()
        if command == "Stop":
            bakes -= 1
            if sum_points > best_points:
                best_man = name_of_baker
                best_points = sum_points
                print(f'{name_of_baker} has {sum_points} points.')
                print(f'{name_of_baker} is the new number 1!')
                sum_points = 0
            else:
                print(f'{name_of_baker} has {sum_points} points.')
                sum_points = 0
            break
        sum_points += int(command)
