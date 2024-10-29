needed_xp = float(input())
count_of_battles = int(input())
xp_total = 0

for battle in range(1, count_of_battles + 1):
    earned_xp = int(input())

    if battle % 3 == 0:
        earned_xp *= 1.15

    if battle % 5 == 0:
        earned_xp *= 0.90

    if battle % 15 == 0:
        earned_xp *= 1.05

    xp_total += round(earned_xp, 2)

    if xp_total >= needed_xp:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break


if xp_total < needed_xp:
    print(f"Player was not able to collect the needed experience, {(needed_xp - xp_total):.2f} more needed.")
