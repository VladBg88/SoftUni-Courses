import math

wall_height = int(input())
wall_width = int(input())
percent_not_to_be_painted = int(input()) / 100
total_space = math.ceil(wall_width * wall_height * 4 * (1 - percent_not_to_be_painted))

painted = 0

while True:
    command = input()
    if command == 'Tired!':
        print(f'{total_space - painted} quadratic m left.')
        break

    painted += int(command)

    if painted == total_space:
        print('All walls are painted! Great job, Pesho!')
        break
    elif painted > total_space:
        print(f'All walls are painted and you have {painted - total_space} l paint left!')
        break
