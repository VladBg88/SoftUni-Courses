TOM_CAPACITY = 30000

free_days = int(input())
work_days = 365 - free_days

free_days_play = free_days * 127
work_days_play = work_days * 63

total_play_time = free_days_play + work_days_play



if total_play_time <= TOM_CAPACITY:
    print('Tom sleeps well')
    print(f'{(TOM_CAPACITY - total_play_time) // 60} hours and {(TOM_CAPACITY - total_play_time) % 60} minutes less for play')
else:
    print(f'Tom will run away')
    print(f"{(total_play_time - TOM_CAPACITY) // 60} hours and {(total_play_time - TOM_CAPACITY) % 60} minutes more for play")
