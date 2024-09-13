import math

days = int(input())
food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

eaten_food = (turtle_food_per_day + cat_food_per_day + dog_food_per_day) * days

if eaten_food <= food_left:
    print(f"{math.floor(food_left - eaten_food)} kilos of food left.")
else:
    print(f"{math.ceil(eaten_food - food_left)} more kilos of food are needed.")
