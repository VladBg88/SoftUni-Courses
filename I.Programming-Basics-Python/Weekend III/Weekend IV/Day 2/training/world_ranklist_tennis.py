import math

POINTS_WIN = 2000
POINTS_FINAL = 1200
POINTS_SEMI_FINAL = 720
LABEL_WIN = 'W'
LABEL_FINAL = 'F'
LABEL_SEMI_FINAL = 'SF'

tournaments = int(input())
starting_points = int(input())
final_points = 0
average_points = 0
win_percentage = 0
win_count = 0

for _ in range(tournaments):
    stage = str(input())
    if stage == LABEL_WIN:
        final_points += POINTS_WIN
        win_count += 1
    elif stage == LABEL_FINAL:
        final_points += POINTS_FINAL
    elif stage == LABEL_SEMI_FINAL:
        final_points += POINTS_SEMI_FINAL

print(f'Final points: {final_points + starting_points}')
print(f'Average points: {math.floor(final_points / tournaments)}')
print(f'{win_count / tournaments * 100:.2f}%')
