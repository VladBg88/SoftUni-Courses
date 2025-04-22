days = int(input())
all_food = float(input())
count_cat_eaten_food = 0
count_dog_eaten_food = 0
count_eaten_biscuits = 0
count_three_days = 3

for i in range(days):
    count_three_days -= 1
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())

    count_cat_eaten_food += cat_eaten_food
    count_dog_eaten_food += dog_eaten_food

    if count_three_days == 0:
        count_eaten_biscuits += round(dog_eaten_food * 0.1) + round(cat_eaten_food * 0.1)

    if count_three_days == 0:
        count_three_days = 3

print(f'Total eaten biscuits: {round(count_eaten_biscuits)}gr.')
print(f'{100 / all_food * (count_dog_eaten_food + count_cat_eaten_food):.2f}% of the food has been eaten.')
print(f'{100 / (count_cat_eaten_food + count_dog_eaten_food) * count_dog_eaten_food:.2f}% eaten from the dog.')
print(f'{100 / (count_cat_eaten_food + count_dog_eaten_food) * count_cat_eaten_food:.2f}% eaten from the cat.')
