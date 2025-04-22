players_dictionary = {}
total_skill = {}

while True:
    command = input()
    if command == 'Season end':
        break

    if '->' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)
        if player not in players_dictionary:
            players_dictionary[player] = {}
        if players_dictionary[player].get(position, 0) < skill:
            players_dictionary[player][position] = skill

    elif 'vs' in command:
        player1, player2 = command.split(' vs ')
        if player1 in players_dictionary and player2 in players_dictionary:
            common_positions = set(players_dictionary[player1]).intersection(players_dictionary[player2])
            if common_positions:
                player1_total = sum(players_dictionary[player1].values())
                player2_total = sum(players_dictionary[player2].values())

                if player1_total > player2_total:
                    del players_dictionary[player2]
                elif player2_total > player1_total:
                    del players_dictionary[player1]

for player, positions in players_dictionary.items():
    total_skill[player] = sum(positions.values())
total_skill = sorted(total_skill.items(), key=lambda x: (-x[1], x[0]))

for player, skill in total_skill:
    print(f'{player}: {skill} skill')
    for position, points in sorted(players_dictionary[player].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {points}")
