PRICES = {
    'Gym': {'m': 42, 'f': 35},
    'Boxing': {'m': 41, 'f': 37},
    'Yoga': {'m': 45, 'f': 42},
    'Zumba': {'m': 34, 'f': 31},
    'Dances': {'m': 51, 'f': 53},
    'Pilates': {'m': 39, 'f': 37}
}

our_money = float(input())
sex = str(input())
age = int(input())
sport = str(input())
total_price = 0

if sport in PRICES and sex in PRICES[sport]:
    total_price = PRICES[sport][sex]

if age <= 19:
    total_price *= 0.8

if total_price <= our_money:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f"You don't have enough money! You need ${total_price - our_money:.2f} more.")
