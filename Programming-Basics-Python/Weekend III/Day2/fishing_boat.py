SPRING_PRICE, SUMMER_AUTUMN_PRICE, WINTER_PRICE = 3000, 4200, 2600

budget = int(input())
season = str(input())
people = int(input())
discount = 0.00
price = 0

if 6 >= people:
    discount = 0.90
if 7 <= people <= 11:
    discount = 0.85
if people >= 12:
    discount = 0.75

if season == 'Spring':
    price = SPRING_PRICE * discount
if season == 'Summer' or season == 'Autumn':
    price = SUMMER_AUTUMN_PRICE * discount
if season == 'Winter':
    price = WINTER_PRICE * discount

if season != 'Autumn' and people % 2 == 0:
    price = price * 0.95

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
if price > budget:
    print(f'Not enough money! You need {price - budget:.2f} leva.')

## Correct code:

group_budget = int(input())
season = input()
fishermen = int(input())

additional_discount = 1.00
trip_price = 0.00

if season == 'Summer' or season == 'Autumn':
    trip_price = 4200
elif season == 'Spring':
    trip_price = 3000
elif season == 'Winter':
    trip_price = 2600

if fishermen <= 6:
    trip_price *= 0.9
elif fishermen <= 11:
    trip_price *= 0.85
else:
    trip_price *= 0.75

if season != 'Autumn' and fishermen % 2 == 0:
    trip_price *= 0.95

if group_budget >= trip_price:
    print(f'Yes! You have {group_budget - trip_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {trip_price - group_budget:.2f} leva.')