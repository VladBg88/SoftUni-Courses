def factorial_division(num_one: int, num_two: int):
    factorial_of_num_one = 1
    for i in range(1, num_one + 1):
        factorial_of_num_one *= i

    factorial_of_num_two = 1
    for i in range(1, num_two + 1):
        factorial_of_num_two *= i

    result = factorial_of_num_one / factorial_of_num_two
    print(f"{result:.2f}")


user_number_a = int(input())
user_number_b = int(input())

factorial_division(user_number_a, user_number_b)
