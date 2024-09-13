import math

days_missing = int(input())
food_left = int(input())
rudolf_1_food = float(input())
rudolf_2_food = float(input())
rudolf_3_food = float(input())

eaten_food = (rudolf_1_food + rudolf_2_food + rudolf_3_food) * days_missing

if food_left >= eaten_food:
    print(f"{math.floor(food_left - eaten_food)} kilos of food left.")
else:
    print(f"{math.ceil(eaten_food - food_left)} more kilos of food are needed.")
