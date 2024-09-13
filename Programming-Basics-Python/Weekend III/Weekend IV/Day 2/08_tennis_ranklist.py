import math

POINTS_WIN = 2000
POINTS_FINAL = 1200
POINTS_SEMI_FINAL = 720
VALUE_WIN = 'W'
VALUE_FINAL = 'f'
VALUE_SEMI_FINAL = 'SF'

tournament_count = int(input())
initial_points = int(input())
acquired_points = 0
win_count = 0


for _ in range(tournament_count):
    state = input().lower().strip()

    if state == VALUE_WIN.lower():
        acquired_points += POINTS_WIN
        win_count += 1
    elif state == VALUE_FINAL.lower():
        acquired_points += POINTS_FINAL
    elif state == VALUE_SEMI_FINAL.lower():
        acquired_points += POINTS_SEMI_FINAL

print(f"Final points: {initial_points + acquired_points}")
print(f"Average points: {math.floor(acquired_points / tournament_count)}")
print(f"{win_count / tournament_count * 100:.2f}%")
