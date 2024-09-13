up_limit_100 = int(input())
up_limit_10 = int(input())
up_limit_1 = int(input())

for first_number in range(2, up_limit_100 + 1):
    for second_number in range(2, up_limit_10 + 1):
        for third_number in range(2, up_limit_1 + 1):
            if first_number % 2 == 0 and third_number % 2 == 0:
                if second_number in (2, 3, 5, 7):
                    print(f'{first_number} {second_number} {third_number}')
