WINTER_DUBAI = 45000
WINTER_SOFIA = 17000
WINTER_LONDON = 24000
SUMMER_DUBAI = 40000
SUMMER_SOFIA = 12500
SUMMER_LONDON = 20250

budget_of_movie = float(input())
destination = str(input())
season = str(input())
days = int(input())
spending = 0

if season == 'Winter':
    if destination == 'Dubai':
        spending = WINTER_DUBAI
    elif destination == 'Sofia':
        spending = WINTER_SOFIA
    elif destination == 'London':
        spending = WINTER_LONDON
elif season == 'Summer':
    if destination == 'Dubai':
        spending = SUMMER_DUBAI
    elif destination == 'Sofia':
        spending = SUMMER_SOFIA
    elif destination == 'London':
        spending = SUMMER_LONDON

total_spending = spending * days

if destination == 'Dubai':
    total_spending *= 0.7
elif destination == 'Sofia':
    total_spending *= 1.25

if budget_of_movie >= total_spending:
    print(f'The budget for the movie is enough! We have {budget_of_movie - total_spending:.2f} leva left!')
elif budget_of_movie < total_spending:
    print(f'The director needs {total_spending - budget_of_movie:.2f} leva more!')
