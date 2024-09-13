SMALL_WATERMELON = 56
SMALL_MANGO = 36.66
SMALL_PINEAPPLE = 42.10
SMALL_RASPBERRY = 20
BIG_WATERMELON = 28.7
BIG_MANGO = 19.6
BIG_PINEAPPLE = 24.80
BIG_RASPBERRY = 15.2

fruit = str(input())
set_size = str(input())
number_of_sets = int(input())
price = 0

if fruit == 'Watermelon':
    if set_size == 'small':
        price = SMALL_WATERMELON * 2
    elif set_size == 'big':
        price = BIG_WATERMELON * 5
elif fruit == 'Mango':
    if set_size == 'small':
        price = SMALL_MANGO * 2
    elif set_size == 'big':
        price = BIG_MANGO * 5
elif fruit == 'Pineapple':
    if set_size == 'small':
        price = SMALL_PINEAPPLE * 2
    elif set_size == 'big':
        price = BIG_PINEAPPLE * 5
elif fruit == 'Raspberry':
    if set_size == 'small':
        price = SMALL_RASPBERRY * 2
    elif set_size == 'big':
        price = BIG_RASPBERRY * 5
else:
    print("Incorrect input!")

total_price = price * number_of_sets
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f'{total_price:.2f} lv.')
