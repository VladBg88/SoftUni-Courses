win_counter = 0
loss_counter = 0
total_matches = 0

while True:
    tournament = str(input())
    if tournament == "End of tournaments":
        break
    command = int(input())
    total_matches += command

    for _ in range(command):
        team_a = int(input())
        team_b = int(input())

        if team_a > team_b:
            print(f"Game {_ + 1} of tournament {tournament}: win with {team_a - team_b} points.")
            win_counter += 1
        elif team_b > team_a:
            print(f"Game {_ + 1} of tournament {tournament}: lost with {team_b - team_a} points.")
            loss_counter += 1

print(f"{100 / total_matches * win_counter:.2f}% matches win")
print(f"{100 / total_matches * loss_counter:.2f}% matches lost")
