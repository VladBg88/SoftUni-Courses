hearthstone_count = 0.0
fornite_count = 0.0
overwatch_count = 0.0
others_count = 0.0

sold_games = int(input())

for i in range(sold_games):
    game_name = str(input())

    if game_name == 'Hearthstone':
        hearthstone_count += 1
    elif game_name == 'Fornite':
        fornite_count += 1
    elif game_name == 'Overwatch':
        overwatch_count += 1
    else:
        others_count += 1

print(f'Hearthstone - {100 / sold_games * hearthstone_count:.2f}%')
print(f'Fornite - {100 / sold_games * fornite_count:.2f}%')
print(f'Overwatch - {100 / sold_games * overwatch_count:.2f}%')
print(f'Others - {100 / sold_games * others_count:.2f}%')
