TAXI_STARTING_PRICE = 0.7
TAXI_DAY_PRICE = 0.79
TAXI_NIGHT_PRICE = 0.9
AUTOBUS_PRICE = 0.09 # minimum distance = 20 km
TRAIN_PRICE = 0.06 # minimum distance = 100 km

kilometers = int(input())
day_night = str(input())
price = 0

if kilometers >= 100:
    price = TRAIN_PRICE
elif kilometers >= 20:
    price = AUTOBUS_PRICE
elif day_night == 'day':
    price = TAXI_DAY_PRICE
elif day_night == 'night':
    price = TAXI_NIGHT_PRICE

total_sum = kilometers * price

if kilometers < 20:
    total_sum += TAXI_STARTING_PRICE

print(f"{total_sum:.2f}")
