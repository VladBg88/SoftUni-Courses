upper_limit_first_digit = int(input())
upper_limit_second_digit = int(input())
upper_limit_third_digit = int(input())

for first_digit in range(2, upper_limit_first_digit + 1, 2):
    for second_digit in range(2, upper_limit_second_digit + 1):

        if second_digit > 1:
            is_prime = True
            for i in range(2, int(second_digit ** 0.5) + 1):
                if second_digit % i == 0:
                    is_prime = False
                    break
            if not is_prime:
                continue
        else:
            continue

        for third_digit in range(2, upper_limit_third_digit + 1, 2):
            print(f"{first_digit} {second_digit} {third_digit}")
