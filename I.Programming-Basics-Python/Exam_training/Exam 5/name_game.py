best_player = ""
best_points = 0
current_player = ""
current_points = 0

while True:
    name = str(input())
    if name == 'Stop':
        break
    name_length = len(name)

    for i in range(name_length):
        number = int(input())
        if number == ord(name[i]):
            current_points += 10
        else:
            current_points += 2

    if current_points >= best_points:
        best_points = current_points
        best_player = name

    current_points = 0

print(f'The winner is {best_player} with {best_points} points!')
