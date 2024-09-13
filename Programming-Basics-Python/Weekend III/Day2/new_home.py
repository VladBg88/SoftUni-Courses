ROSES_PRICE, DAHLIAS_PRICE, TULIPS_PRICE, NARCISSUS_PRICE, GLADIOLUS_PRICE = 5, 3.80, 2.80, 3, 2.50

type_of_flower = str(input())
pcs_of_flowers = float(input())
budget = float(input())
discount = 0
total_price = 0

if type_of_flower == 'Roses':
    total_price = pcs_of_flowers * ROSES_PRICE
    if pcs_of_flowers > 80:
        total_price = total_price * 0.9
if type_of_flower == 'Dahlias':
    total_price = pcs_of_flowers * DAHLIAS_PRICE
    if pcs_of_flowers > 90:
        total_price = total_price * 0.85
if type_of_flower == 'Tulips':
    total_price = pcs_of_flowers * TULIPS_PRICE
    if pcs_of_flowers > 80:
        total_price = total_price * 0.85
if type_of_flower == 'Narcissus':
    total_price = pcs_of_flowers * NARCISSUS_PRICE
    if pcs_of_flowers < 120:
        total_price = total_price * 1.15
if type_of_flower == 'Gladiolus':
    total_price = pcs_of_flowers * GLADIOLUS_PRICE
    if pcs_of_flowers < 80:
        total_price = total_price * 1.2

if budget >= total_price:
    print(f'Hey, you have a great garden with {pcs_of_flowers:.0f} {type_of_flower} and {budget - total_price:.2f} leva left.')
if total_price > budget:
    print(f'Not enough money, you need {total_price - budget:.2f} leva more.')
