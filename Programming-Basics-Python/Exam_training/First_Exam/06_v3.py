upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

for number_one in range(2, upper_limit_first_number + 1, 2):
    for number_two in range(2, upper_limit_second_number + 1):
        for number_three in range(2, upper_limit_third_number + 1, 2):
            if number_two in (2, 3, 5, 7):
                print(f"{number_one} {number_two} {number_three}")
