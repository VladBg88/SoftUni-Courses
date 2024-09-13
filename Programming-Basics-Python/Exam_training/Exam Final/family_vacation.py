budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_extra_spends = 1 - int(input()) / 100

if nights > 7:
    price_per_night *= 0.95

budget *= percent_extra_spends
spending = price_per_night * nights

if budget >= spending:
    print(f"Ivanovi will be left with {budget - spending:.2f} leva after vacation.")
else:
    print(f"{spending - budget:.2f} leva needed.")
