LARGE_RED = 16
LARGE_GREEN = 12
LARGE_YELLOW = 9
MEDIUM_RED = 13
MEDIUM_GREEN = 9
MEDIUM_YELLOW = 7
SMALL_RED = 9
SMALL_GREEN = 8
SMALL_YELLOW = 5

size = str(input())
color = str(input())
number = int(input())
egg_price = 0

if size == 'Large':
    if color == 'Red':
        egg_price = LARGE_RED
    elif color == 'Green':
        egg_price = LARGE_GREEN
    elif color == 'Yellow':
        egg_price = LARGE_YELLOW
if size == 'Medium':
    if color == 'Red':
        egg_price = MEDIUM_RED
    elif color == 'Green':
        egg_price = MEDIUM_GREEN
    elif color == 'Yellow':
        egg_price = MEDIUM_YELLOW
if size == 'Small':
    if color == 'Red':
        egg_price = SMALL_RED
    elif color == 'Green':
        egg_price = SMALL_GREEN
    elif color == 'Yellow':
        egg_price = SMALL_YELLOW

total_price = egg_price * number * 0.65
print(f'{total_price:.2f} leva.')
