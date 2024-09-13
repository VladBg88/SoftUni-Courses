budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extra_spends = int(input())

hotel_charge = nights * price_per_night
extra_spends = budget * (percent_extra_spends / 100)

if nights > 7:
    hotel_charge *= 0.95

total_price = hotel_charge + extra_spends

if budget >= total_price:
    print(f'Ivanovi will be left with {budget - total_price:.2f} leva after vacation.')
else:
    print(f'{total_price - budget:.2f} leva needed.')
