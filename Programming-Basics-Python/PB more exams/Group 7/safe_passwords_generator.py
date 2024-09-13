a = int(input())
b = int(input())
max_generated_passwords = int(input())
a_symbol = 35
b_symbol = 64
x_symbol = 1
y_symbol = 1

while True:
    print(f'{chr(a_symbol)}{chr(b_symbol)}{x_symbol}{y_symbol}{chr(b_symbol)}{chr(a_symbol)}', end='|')
    max_generated_passwords -= 1

    if max_generated_passwords == 0:
        break

    a_symbol += 1
    b_symbol += 1

    if a_symbol > 55:
        a_symbol = 35

    if b_symbol > 96:
        b_symbol = 64

    if y_symbol < b:
        y_symbol += 1
    elif x_symbol < a:
        x_symbol += 1
        y_symbol = 1
    else:
        break

