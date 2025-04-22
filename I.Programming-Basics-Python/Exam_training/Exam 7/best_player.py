best_player = ""
best_score = 0

while True:
    player_name = str(input())
    if player_name == 'END':
        break
    goals = int(input())

    if goals > best_score:
        best_player = player_name
        best_score = goals

    if goals > 9:
        break

print(f'{best_player} is the best player!')

if best_score > 2:
    print(f'He has scored {best_score} goals and made a hat-trick !!!')
else:
    print(f'He has scored {best_score} goals.')
