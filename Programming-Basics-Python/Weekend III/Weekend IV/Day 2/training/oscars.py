actor_name = str(input())
academy_points = float(input())
jury_number = int(input())
total_points = academy_points

for _ in range(jury_number):
    jury_member_name = str(input())
    jury_member_points = float(input())
    total_points += len(jury_member_name) * jury_member_points / 2
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        exit()

print(f"Sorry, {actor_name} you need {1250.5 - total_points:.1f} more!")
