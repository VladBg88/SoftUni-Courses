user_list = input().split(', ')
positive_list = [digit for digit in user_list if int(digit) >= 0]
negative_list = [digit for digit in user_list if int(digit) < 0]
even_list = [digit for digit in user_list if int(digit) % 2 == 0]
odd_list = [digit for digit in user_list if int(digit) % 2 != 0]

print(f"Positive: {', '.join(positive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")
