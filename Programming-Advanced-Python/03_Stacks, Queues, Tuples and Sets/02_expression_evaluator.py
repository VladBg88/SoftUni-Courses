from math import floor

user_input = (input().split())
final_result = int(user_input.pop(0))
current_numbers = []

for element in user_input:
    try:
        number = int(element)
        current_numbers.append(number)
    except ValueError:
        if element == '+':
            for digit in current_numbers:
                final_result += digit
            current_numbers = []
        elif element == '-':
            for digit in current_numbers:
                final_result -= digit
            current_numbers = []
        elif element == '/':
            for digit in current_numbers:
                final_result = floor(final_result / digit)
            current_numbers = []
        elif element == '*':
            for digit in current_numbers:
                final_result *= digit
            current_numbers = []

print(final_result)

