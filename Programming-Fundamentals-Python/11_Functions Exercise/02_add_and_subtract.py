def sum_numbers(a, b):
    return a + b


def subtract():
    return sum_numbers(first_number, second_number) - third_number


def add_and_subtract():
    print(subtract())


first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract()
