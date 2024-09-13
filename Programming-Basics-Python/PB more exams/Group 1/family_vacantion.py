budget = float(input())
days_reservation = int(input())
price_per_night = float(input())
extra_charges = int(input()) / 100

if days_reservation > 7:
    price_per_night = price_per_night * 0.95

extra_charges_sum = budget * extra_charges
spending = days_reservation * price_per_night + extra_charges_sum

if budget >= spending:
    print(f"Ivanovi will be left with {budget - spending:.2f} leva after vacation.")
else:
    print(f"{spending - budget:.2f} leva needed.")
