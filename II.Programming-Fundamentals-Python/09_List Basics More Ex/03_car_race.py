sequence_of_numbers = input().split()
middle = len(sequence_of_numbers) // 2
first_racer_stage = sequence_of_numbers[:middle]
second_racer_stage = sequence_of_numbers[middle + 1:]
second_racer_stage.reverse()
first_racer_total_time = 0
second_racer_total_time = 0

for track in first_racer_stage:
    if int(track) == 0 and first_racer_total_time > 0:
        first_racer_total_time *= 0.8
    else:
        first_racer_total_time += int(track)

for track in second_racer_stage:
    if int(track) == 0 and second_racer_total_time > 0:
        second_racer_total_time *= 0.8
    else:
        second_racer_total_time += int(track)

if first_racer_total_time < second_racer_total_time:
    print(f'The winner is left with total time: {first_racer_total_time:.1f}')
else:
    print(f'The winner is right with total time: {second_racer_total_time:.1f}')
