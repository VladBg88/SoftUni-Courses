season = str(input())
kilometers_per_month = float(input())

if 10000 < kilometers_per_month <= 20000:
    earning = 1.45
elif kilometers_per_month > 5000:
    if season == 'Spring' or season == 'Autumn':
        earning = 0.95
    elif season == 'Summer':
        earning = 1.10
    elif season == 'Winter':
        earning = 1.25
elif kilometers_per_month > 0:
    if season == 'Spring' or season == 'Autumn':
        earning = 0.75
    elif season == 'Summer':
        earning = 0.90
    elif season == 'Winter':
        earning = 1.05

total_earning = kilometers_per_month * earning * 4 * 0.9

print(f'{total_earning:.2f}')
