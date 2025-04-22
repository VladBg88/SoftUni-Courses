FRANCE_21_23 = 30
FRANCE_24_27 = 35
FRANCE_28_31 = 40
ITALY_21_23 = 28
ITALY_24_27 = 32
ITALY_28_31 = 39
GERMANY_21_23 = 32
GERMANY_24_27 = 37
GERMANY_28_31 = 43

destination = str(input())
date = str(input())
nights = int(input())
total_price = 0

if destination == 'France':
    if date == '21-23':
        total_price = FRANCE_21_23
    elif date == '24-27':
        total_price = FRANCE_24_27
    elif date == '28-31':
        total_price = FRANCE_28_31
elif destination == 'Italy':
    if date == '21-23':
        total_price = ITALY_21_23
    elif date == '24-27':
        total_price = ITALY_24_27
    elif date == '28-31':
        total_price = ITALY_28_31
elif destination == 'Germany':
    if date == '21-23':
        total_price = GERMANY_21_23
    elif date == '24-27':
        total_price = GERMANY_24_27
    elif date == '28-31':
        total_price = GERMANY_28_31

total_price *= nights

print(f'Easter trip to {destination} : {total_price:.2f} leva.')
