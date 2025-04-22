ESPRESSO_WITHOUT_SUGAR = 0.9
ESPRESSO_NORMAL = 1
ESPRESSO_EXTRA_SUGAR = 1.2
CAPPUCCINO_WITHOUT_SUGAR = 1
CAPPUCCINO_NORMAL = 1.2
CAPPUCCINO_EXTRA_SUGAR = 1.6
TEA_WITHOUT_SUGAR = 0.5
TEA_NORMAL = 0.6
TEA_EXTRA_SUGAR = 0.7

drink = str(input())
sugar = str(input())
number_of_drink = int(input())
price = 0

if drink == 'Espresso':
    if sugar == 'Without':
        price = ESPRESSO_WITHOUT_SUGAR
    elif sugar == 'Normal':
        price = ESPRESSO_NORMAL
    elif sugar == 'Extra':
        price = ESPRESSO_EXTRA_SUGAR
elif drink == 'Cappuccino':
    if sugar == 'Without':
        price = CAPPUCCINO_WITHOUT_SUGAR
    elif sugar == 'Normal':
        price = CAPPUCCINO_NORMAL
    elif sugar == 'Extra':
        price = CAPPUCCINO_EXTRA_SUGAR
elif drink == 'Tea':
    if sugar == 'Without':
        price = TEA_WITHOUT_SUGAR
    elif sugar == 'Normal':
        price = TEA_NORMAL
    elif sugar == 'Extra':
        price = TEA_EXTRA_SUGAR

if sugar == 'Without':
    price *= 0.65

if drink == 'Espresso' and number_of_drink > 4:
    price *= 0.75

total_price = price * number_of_drink

if total_price > 15:
    total_price *= 0.8

print(f'You bought {number_of_drink} cups of {drink} for {total_price:.2f} lv.')
