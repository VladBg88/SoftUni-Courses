budget = float(input())
season = str(input())
expenses = 0.0
place = ""
camp_or_hotel = ""

if budget <= 100:
    place = 'Bulgaria'
    if season == 'summer':
        expenses = budget * 0.30
    if season == 'winter':
        expenses = budget * 0.70
elif budget <= 1000:
    place = 'Balkans'
    if season == 'summer':
        expenses = budget * 0.40
    if season == 'winter':
        expenses = budget * 0.80
else:
    place = 'Europe'
    expenses = budget * 0.90

if season == 'summer' and place != 'Europe':
    camp_or_hotel = 'Camp'
elif season == 'winter' or place == 'Europe':
    camp_or_hotel = 'Hotel'

print(f'Somewhere in {place}')
print(f'{camp_or_hotel} - {expenses:.2f}')
