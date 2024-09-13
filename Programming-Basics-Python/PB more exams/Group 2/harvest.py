import math

field = int(input())
grape_per_square_meter = float(input())
needed_litres_wine = float(input())
number_of_workers = int(input())

total_grape = field * grape_per_square_meter
litres_of_wine = (total_grape * 0.4) / 2.5

if needed_litres_wine <= litres_of_wine:
    print(f"Good harvest this year! Total wine: {int(litres_of_wine)} liters.")
    print(f"{math.ceil(litres_of_wine - needed_litres_wine)} liters left -> {math.ceil((litres_of_wine - needed_litres_wine) / number_of_workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {int(needed_litres_wine - litres_of_wine)} liters wine needed.")
