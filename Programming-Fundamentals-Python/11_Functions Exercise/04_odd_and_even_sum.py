def odd_even_sum(number: str):
    odd_sum = 0
    even_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


user_number = input()
odd_even_sum(user_number)
