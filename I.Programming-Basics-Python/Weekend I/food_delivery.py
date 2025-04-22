CHICKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETARIAN_MENU = 8.15
DELIVERY_TAX = 2.50
DESERT_MENU = 20/100

count_chicken = int(input())
count_fish = int(input())
count_vegetarian = int(input())

total_chicken = count_chicken * CHICKEN_MENU
total_fish = count_fish * FISH_MENU
total_vegetarian = count_vegetarian * VEGETARIAN_MENU

all_food_price = total_vegetarian + total_fish + total_chicken

desert = all_food_price * DESERT_MENU

final_price = all_food_price + desert + DELIVERY_TAX

print(final_price)
