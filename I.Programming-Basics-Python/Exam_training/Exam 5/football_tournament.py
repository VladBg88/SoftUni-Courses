team_name = str(input())
matches_number = int(input())

if matches_number == 0:
    print(f"{team_name} hasn't played any games during this season.")
    exit()

win_count = 0
draw_count = 0
loss_count = 0

for i in range(matches_number):
    result = str(input())

    if result == 'W':
        win_count += 1
    elif result == 'D':
        draw_count += 1
    elif result == 'L':
        loss_count += 1

print(f'{team_name} has won {win_count * 3 + draw_count} points during this season.')
print('Total stats:')
print(f'## W: {win_count}')
print(f'## D: {draw_count}')
print(f'## L: {loss_count}')
print(f'Win rate: {100 / matches_number * win_count:.2f}%')
