def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


upper_limit_first_digit = int(input())
upper_limit_second_digit = int(input())
upper_limit_third_digit = int(input())

for first_digit in range(2, upper_limit_first_digit + 1, 2):
    for second_digit in range(2, upper_limit_second_digit + 1):
        if not is_prime(second_digit):
            continue
        for third_digit in range(2, upper_limit_third_digit + 1, 2):
            print(f"{first_digit} {second_digit} {third_digit}")
