import math

name_of_serial = str(input())
number_of_seasons = int(input())
number_of_episodes = int(input())
time_of_episode = float(input())

time_of_episode *= 1.2
extra_time = number_of_seasons * 10
total_time = time_of_episode * number_of_episodes * number_of_seasons + extra_time

print(f'Total time needed to watch the {name_of_serial} series is {math.floor(total_time)} minutes.')
