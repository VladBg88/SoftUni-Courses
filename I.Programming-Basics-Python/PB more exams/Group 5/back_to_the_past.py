money_earned = float(input())
year = int(input())
ivancho_years = 18
spending = 0

for i in range(1800, year + 1):
    if i % 2 == 0:
        spending += 12000
    else:
        spending += 12000 + (50 * ivancho_years)

    ivancho_years += 1

if money_earned >= spending:
    print(f'Yes! He will live a carefree life and will have {money_earned - spending:.2f} dollars left.')
else:
    print(f'He will need {spending - money_earned:.2f} dollars to survive.')
