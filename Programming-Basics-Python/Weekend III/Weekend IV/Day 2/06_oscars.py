NOMINATION_ENTRY_POINTS = 1250.5

actor_name = input()
academy_points = float(input())
juror_count = int(input())
actor_total_points = academy_points

for _ in range(juror_count):
    juror_name = input()
    juror_points = float(input())
    juror_final_points = len(juror_name) * juror_points / 2
    actor_total_points += juror_final_points

    if actor_total_points > NOMINATION_ENTRY_POINTS:
        break

if actor_total_points > NOMINATION_ENTRY_POINTS:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_total_points:.1f}!")
else:
    points_needed = NOMINATION_ENTRY_POINTS - actor_total_points
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
