letters = int(input())

for char_one in range(97, 97 + letters):
    for char_two in range(97, 97 + letters):
        for char_three in range(97, 97 + letters):
            print(f'{chr(char_one)}{chr(char_two)}{chr(char_three)}')
