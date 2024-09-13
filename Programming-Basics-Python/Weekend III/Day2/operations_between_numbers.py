from math import ceil

N1 = int(input())
N2 = int(input())
operator = str(input())
result = 0
even_or_odd = ""

if operator == '+':
    result = N1 + N2
elif operator == '-':
    result = N1 - N2
elif operator == '*':
    result = N1 * N2

if operator == '+' or operator == '-' or operator == '*':
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"

if operator == '/' and N2 != 0:
    result = N1 / N2
elif operator == '/' and N2 == 0:
    print(f'Cannot divide {N1} by zero')

if operator == '%' and N2 != 0:
    result = N1 % N2
elif operator == '%' and N2 == 0:
    print(f'Cannot divide {N1} by zero')

if operator == '+' or operator == '-' or operator == '*':
    print(f'{N1} {operator} {N2} = {ceil(result)} - {even_or_odd}')
elif operator == '/' and N2 != 0:
    print(f'{N1} {operator} {N2} = {result:.2f}')
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
elif operator == '%' and N2 != 0:
    print(f'{N1} {operator} {N2} = {result:.0f}')
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
