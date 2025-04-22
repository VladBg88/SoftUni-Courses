# 1 easter_bread -> 3 guests
# 2 eggs -> 1 guest
import math

EASTER_BREAD_PRICE = 4
EGG_PRICE = 0.45

guests = int(input())
budget = int(input())

needed_eggs = guests * 2
needed_easter_bread = math.ceil(guests / 3)
total_price = needed_eggs * EGG_PRICE + needed_easter_bread * EASTER_BREAD_PRICE

if budget >= total_price:
    print(f"Lyubo bought {needed_easter_bread} Easter bread and {needed_eggs} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")
