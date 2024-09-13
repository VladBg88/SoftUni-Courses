guests = int(input())
price_per_guest = float(input())
budget = float(input())

if 20 < guests:
    price_per_guest *= 0.75
elif 15 < guests <= 20:
    price_per_guest *= 0.8
elif 10 <= guests <= 15:
    price_per_guest *= 0.85

spending = guests * price_per_guest + budget * 0.1
if budget >= spending:
    print(f"It is party time! {budget - spending:.2f} leva left.")
else:
    print(f"No party! {spending - budget:.2f} leva needed.")
