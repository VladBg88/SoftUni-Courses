WICK_DRINK = 12
WICK_POPCORN = 15
WICK_MENU = 19
STARW_DRINK = 18
STARW_POPCORN = 25
STARW_MENU = 30
JUMANJI_DRINK = 9
JUMANJI_POPCRON = 11
JUMANJI_MENU = 14

movie = str(input())
packet = str(input())
tickets = int(input())
price = 0

if movie == 'John Wick':
    if packet == 'Drink':
        price = WICK_DRINK
    elif packet == 'Popcorn':
        price = WICK_POPCORN
    elif packet == 'Menu':
        price = WICK_MENU
elif movie == 'Star Wars':
    if packet == 'Drink':
        price = STARW_DRINK
    elif packet == 'Popcorn':
        price = STARW_POPCORN
    elif packet == 'Menu':
        price = STARW_MENU
elif movie == 'Jumanji':
    if packet == 'Drink':
        price = JUMANJI_DRINK
    elif packet == 'Popcorn':
        price = JUMANJI_POPCRON
    elif packet == 'Menu':
        price = JUMANJI_MENU

if movie == 'Star Wars' and tickets > 3:
    price *= 0.7
elif movie == 'Jumanji' and tickets == 2:
    price *= 0.85

total_price = price * tickets

print(f'Your bill is {total_price:.2f} leva.')

