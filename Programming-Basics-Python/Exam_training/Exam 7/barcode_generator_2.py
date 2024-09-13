start = int(input())
end = int(input())

# Extract digits of start
first_start, second_start, third_start, fourth_start = map(int, str(start).zfill(4))

# Extract digits of end
first_end, second_end, third_end, fourth_end = map(int, str(end).zfill(4))

# Loop through each digit position
for num_1 in range(first_start, first_end + 1):
    if num_1 % 2 == 0:
        continue
    for num_2 in range(second_start if num_1 == first_start else 1, (second_end + 1) if num_1 == first_end else 10):
        if num_2 % 2 == 0:
            continue
        for num_3 in range(third_start if num_1 == first_start and num_2 == second_start else 1, (third_end + 1) if num_1 == first_end and num_2 == second_end else 10):
            if num_3 % 2 == 0:
                continue
            for num_4 in range(fourth_start if num_1 == first_start and num_2 == second_start and num_3 == third_start else 1, (fourth_end + 1) if num_1 == first_end and num_2 == second_end and num_3 == third_end else 10):
                if num_4 % 2 == 0:
                    continue
                print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')
