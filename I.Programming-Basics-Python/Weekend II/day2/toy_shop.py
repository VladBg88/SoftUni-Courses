PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

price_excursion = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
teddy_bear_quantity = int(input())
minions_quantity = int(input())
truck_quantity = int(input())

puzzle_sum = puzzle_quantity * PUZZLE
doll_sum = doll_quantity * DOLL
teddy_bear_sum = teddy_bear_quantity * TEDDY_BEAR
minions_sum = minions_quantity * MINION
truck_sum = truck_quantity * TRUCK

earning = puzzle_sum + doll_sum + teddy_bear_sum + minions_sum + truck_sum

all_orders = puzzle_quantity + doll_quantity + teddy_bear_quantity + minions_quantity + truck_quantity

if all_orders >= 50:
    earning = earning * 0.75

earning = earning * 0.90

if earning >= price_excursion:
    left_money = earning - price_excursion

if earning >= price_excursion:
    left_money = earning - price_excursion
    print(f'Yes! {left_money:.2f} lv left.')
else:
    needed_money = price_excursion - earning
    print(f'Not enough money! {needed_money:.2f} lv needed.')
