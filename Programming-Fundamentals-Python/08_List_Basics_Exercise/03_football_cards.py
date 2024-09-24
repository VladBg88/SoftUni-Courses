cards_sequence = input()

team_A = set()
team_B = set()

max_players = 11
min_players = 7

cards = cards_sequence.split()

for card in cards:
    team, player = card.split('-')
    player = int(player)

    if team == "A" and player not in team_A:
        team_A.add(player)

    elif team == "B" and player not in team_B:
        team_B.add(player)


    if (max_players - len(team_A) < min_players) or (max_players - len(team_B) < min_players):
        print(f"Team A - {max_players - len(team_A)}; Team B - {max_players - len(team_B)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {max_players - len(team_A)}; Team B - {max_players - len(team_B)}")
