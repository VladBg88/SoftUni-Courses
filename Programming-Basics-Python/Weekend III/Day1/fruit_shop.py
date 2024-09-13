BANANA_1 = 2.50
APPLE_1 = 1.20
ORANGE_1 = 0.85
GRAPEFRUIT_1 = 1.45
KIWI_1 = 2.70
PINEAPPLE_1 = 5.50
GRAPES_1 = 3.85

BANANA_2 = 2.70
APPLE_2 = 1.25
ORANGE_2 = 0.90
GRAPEFRUIT_2 = 1.60
KIWI_2 = 3.00
PINEAPPLE_2 = 5.60
GRAPES_2: float = 4.20

fruit = str(input())
day = str(input())
quantity = float(input())
price = 0.00

if day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = BANANA_2
    if fruit == 'apple':
        price = APPLE_2
    if fruit == 'orange':
        price = ORANGE_2
    if fruit == 'grapefruit':
        price = GRAPEFRUIT_2
    if fruit == 'kiwi':
        price = KIWI_2
    if fruit == 'pineapple':
        price = PINEAPPLE_2
    if fruit == 'grapes':
        price = GRAPES_2

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = BANANA_1
    if fruit == 'apple':
        price = APPLE_1
    if fruit == 'orange':
        price = ORANGE_1
    if fruit == 'grapefruit':
        price = GRAPEFRUIT_1
    if fruit == 'kiwi':
        price = KIWI_1
    if fruit == 'pineapple':
        price = PINEAPPLE_1
    if fruit == 'grapes':
        price = GRAPES_1

price = price * quantity

if price == 0:
    print("error")
elif price > 0:
    print(f'{price:.2f}')
