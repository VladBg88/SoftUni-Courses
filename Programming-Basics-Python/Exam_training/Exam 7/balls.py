import math

RED = 5
ORANGE = 10
YELLOW = 15
WHITE = 20

total_points_count = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
other_count = 0
divided_count = 0

number_of_balls = int(input())

for i in range(number_of_balls):
    color = input()

    if color == 'red':
        red_count += 1
        total_points_count += RED
    elif color == 'orange':
        orange_count += 1
        total_points_count += ORANGE
    elif color == 'yellow':
        yellow_count += 1
        total_points_count += YELLOW
    elif color == 'white':
        white_count += 1
        total_points_count += 20
    elif color == 'black':
        total_points_count = math.floor(total_points_count / 2)
        divided_count += 1
    else:
        other_count += 1

print(f'Total points: {total_points_count}')
print(f'Red balls: {red_count}')
print(f'Orange balls: {orange_count}')
print(f'Yellow balls: {yellow_count}')
print(f'White balls: {white_count}')
print(f'Other colors picked: {other_count}')
print(f'Divides from black balls: {divided_count}')
