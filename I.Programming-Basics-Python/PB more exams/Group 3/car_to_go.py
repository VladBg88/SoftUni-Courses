budget = float(input())
season = str(input())
car_class = 'Class: Invalid input!'
car_type = 'Car type: Invalid input!'
price = 0

if budget > 500:
    car_class = 'Luxury class'
    car_type = 'Jeep'
    price = budget * 0.9
elif budget > 100:
    car_class = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.45
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.8
elif budget > 0:
    car_class = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        price = budget * 0.35
    elif season == 'Winter':
        car_type = 'Jeep'
        price = budget * 0.65

print(car_class)
print(f'{car_type} - {price:.2f}')
