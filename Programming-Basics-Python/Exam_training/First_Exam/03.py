number_of_dancers = int(input())
points = float(input())
season = str.lower(input()).strip()
place = str.lower(input()).strip()
money_earned = 0
money_donated = 0.25

if place == 'bulgaria':
    money_earned = points * number_of_dancers
elif place == 'abroad':
    money_earned = (number_of_dancers * points) * 1.5

tax = 1

if place == 'bulgaria':
    if season == 'summer':
        tax = 0.95
    elif season == 'winter':
        tax = 0.92
elif place == 'abroad':
    if season == 'summer':
        tax = 0.9
    elif season == 'winter':
        tax = 0.85

money_after_taxes = money_earned * tax
money_after_donating = money_after_taxes * money_donated

print(f"Charity - {money_after_taxes - money_after_donating:.2f}")
print(f"Money per dancer - {money_after_donating / number_of_dancers:.2f}")
