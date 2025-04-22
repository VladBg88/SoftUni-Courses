def max_min_sum(custom_list: list):
    sequence_of_numbers = [int(x) for x in custom_list]
    max_number = max(sequence_of_numbers)
    min_number = min(sequence_of_numbers)
    sum_number = sum(sequence_of_numbers)

    print(f"The minimum number is {min_number}")
    print(f"The maximum number is {max_number}")
    print(f"The sum number is: {sum_number}")


user_sequence_of_numbers = input().split()
max_min_sum(user_sequence_of_numbers)
