PRICE = {
    'one': {'Small': 9.98, 'Middle': 18.99, 'Large': 25.98, 'ExtraLarge': 35.99},
    'two': {'Small': 8.58, 'Middle': 17.09, 'Large': 23.59, 'ExtraLarge': 31.79}
}

period = str(input())
type_of_agreement = str(input())
mobile_internet = str(input())
month = int(input())
price = 0
internet_charge = 0.0

if period in PRICE and type_of_agreement in PRICE[period]:
    price = PRICE[period][type_of_agreement]

if mobile_internet == 'yes':
    if price > 30:
        internet_charge = 3.85
    elif price > 10:
        internet_charge = 4.35
    elif price > 0:
        internet_charge = 5.5

price += internet_charge
total_price = price * month

if period == 'two':
    total_price *= 0.9625

print(f'{total_price:.2f} lv.')
