LEFT_RANGE_BOUNDARY = 1111
RIGHT_RANGE_BOUNDARY = 9999

number = int(input())

for current_number in range(LEFT_RANGE_BOUNDARY, RIGHT_RANGE_BOUNDARY + 1):
    str_from_number = str(current_number)
    is_special = True

    for _, value in enumerate(str_from_number):
        int_val = int(value)
        if int_val == 0:
            is_special = False
            break

        if number % int(value) != 0:
            is_special = False
            break

    if is_special:
        print(current_number, end=" ")
