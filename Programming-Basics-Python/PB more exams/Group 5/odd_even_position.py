import sys

numbers = int(input())
count_odd_sum = 0.0
count_odd_min = sys.maxsize
count_odd_max = -sys.maxsize
count_even_sum = 0.0
count_even_min = sys.maxsize
count_even_max = -sys.maxsize

for i in range(1, numbers + 1):
    customer_input = float(input())

    if i % 2 == 0:
        count_even_sum += customer_input
        if customer_input > count_even_max:
            count_even_max = customer_input
        if customer_input < count_even_min:
            count_even_min = customer_input
    else:
        count_odd_sum += customer_input
        if customer_input > count_odd_max:
            count_odd_max = customer_input
        if customer_input < count_odd_min:
            count_odd_min = customer_input

print(f'OddSum={count_odd_sum:.2f},')

if count_odd_min == sys.maxsize:
    print(f'OddMin=No,')
else:
    print(f'OddMin={count_odd_min:.2f},')

if count_odd_max == -sys.maxsize:
    print(f'OddMax=No,')
else:
    print(f'OddMax={count_odd_max:.2f},')
print(f'EvenSum={count_even_sum:.2f},')
if count_even_min == sys.maxsize:
    print(f'EvenMin=No,')
else:
    print(f'EvenMin={count_even_min:.2f},')
if count_even_max == -sys.maxsize:
    print(f'EvenMax=No')
else:
    print(f'EvenMax={count_even_max:.2f}')
