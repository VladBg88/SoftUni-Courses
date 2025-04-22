budget = float(input())
season = str(input())

if budget > 3000:
    accommodation = 'Hotel'
    price = budget * 0.9
    if season == 'Summer':
        place = 'Alaska'
    elif season == 'Winter':
        place = 'Morocco'
elif budget > 1000:
    accommodation = 'Hut'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.8
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.6
elif budget > 0:
    accommodation = 'Camp'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        place = 'Morocco'
        price = budget * 0.45

print(f'{place} - {accommodation} - {price:.2f}')
