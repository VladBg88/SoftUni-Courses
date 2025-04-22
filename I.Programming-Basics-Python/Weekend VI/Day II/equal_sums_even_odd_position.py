number_1 = int(input())
number_2 = int(input())

for current_number in range(number_1, number_2 + 1):
    sum_even = 0
    sum_odd = 0
    str_from_number = str(current_number)
    for index, value in enumerate(str_from_number):
        if index % 2 == 0:
            sum_even += int(value)
        else:
            sum_odd += int(value)
    if sum_even == sum_odd:
        print(current_number, end=" ")
