from math import ceil

movie_name = input()
episode_length = int(input())
break_length = int(input())

eating = break_length / 8
relax = break_length / 4
free_time = break_length - eating - relax

if free_time >= episode_length:
    bonus_time = break_length - eating - relax - episode_length
    print(f'You have enough time to watch {movie_name} and left with {ceil(bonus_time)} minutes free time.')
else:
    needed_time = eating + relax + episode_length - break_length
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(needed_time)} more minutes.")
