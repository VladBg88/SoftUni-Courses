first_user_number = int(input())
second_user_number = int(input())
third_user_number = int(input())


def smallest(a, b, c):
    list_of_three_numbers = [a, b, c]
    result = min(list_of_three_numbers)
    return result


print(smallest(first_user_number, second_user_number, third_user_number))
