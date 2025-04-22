PRICE_LITER_FUEL = 2.1
PRICE_GUIDE = 100

budget = float(input())
litres_fuel_needed = float(input())
day_of_week = str(input())
promo = 1

if day_of_week == 'Saturday':
    promo = 0.9
elif day_of_week == 'Sunday':
    promo = 0.8

fuel_spending = litres_fuel_needed * PRICE_LITER_FUEL
spending = (fuel_spending + PRICE_GUIDE) * promo

if spending <= budget:
    print(f'Safari time! Money left: {budget - spending:.2f} lv. ')
else:
    print(f'Not enough money! Money needed: {spending - budget:.2f} lv.')
