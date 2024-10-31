hidden_string = input()
non_numbers_list = [character for character in hidden_string if not character.isdigit()]
numbers_list = [int(digit) for digit in hidden_string if digit.isdigit()]
take_even_list = [even_digit for index, even_digit in enumerate(numbers_list) if index % 2 == 0]
skip_odd_list = [even_digit for index, even_digit in enumerate(numbers_list) if index % 2 != 0]

result_string = []

for i in range(len(take_even_list)):
    if take_even_list[i] > 0:
        take = non_numbers_list[:take_even_list[i]]
        result_string += take
        non_numbers_list = non_numbers_list[take_even_list[i]:]
    if skip_odd_list[i] <= len(non_numbers_list) - 1:
        non_numbers_list = non_numbers_list[skip_odd_list[i]:]

print(''.join(map(str, result_string)))
