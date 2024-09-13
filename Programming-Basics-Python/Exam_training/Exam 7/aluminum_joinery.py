SIZE_90X130_PRICE = 110
SIZE_100X150_PRICE = 140
SIZE_130X180_PRICE = 190
SIZE_200X300_PRICE = 250

number_of_windows = int(input())
type_of_window = str(input())
delivery_type = str(input())

price = 0
promo = 1

if number_of_windows < 10:
    print('Invalid order')
    exit()

if type_of_window == '90X130':
    price = SIZE_90X130_PRICE
    if number_of_windows > 60:
        promo = 0.92
    elif number_of_windows > 30:
        promo = 0.95
elif type_of_window == '100X150':
    price = SIZE_100X150_PRICE
    if number_of_windows > 80:
        promo = 0.9
    elif number_of_windows > 40:
        promo = 0.94
elif type_of_window == '130X180':
    price = SIZE_130X180_PRICE
    if number_of_windows > 50:
        promo = 0.88
    elif number_of_windows > 20:
        promo = 0.93
elif type_of_window == '200X300':
    price = SIZE_200X300_PRICE
    if number_of_windows > 50:
        promo = 0.86
    elif number_of_windows > 25:
        promo = 0.91

total_price = price * number_of_windows * promo

if delivery_type == 'With delivery':
    total_price += 60

if number_of_windows > 99:
    total_price *= 0.96

print(f'{total_price:.2f} BGN')
