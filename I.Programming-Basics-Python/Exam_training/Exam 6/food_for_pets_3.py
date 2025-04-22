days = int(input())
all_food = float(input())
count_cat_eaten_food = 0
count_dog_eaten_food = 0
count_eaten_biscuits = 0

for i in range(1, days + 1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())

    count_cat_eaten_food += cat_eaten_food
    count_dog_eaten_food += dog_eaten_food

    if i % 3 == 0:
        count_eaten_biscuits += (dog_eaten_food + cat_eaten_food) * 0.1

total_eaten_food = count_cat_eaten_food + count_dog_eaten_food

print(f'Total eaten biscuits: {round(count_eaten_biscuits)}gr.')
print(f'{(total_eaten_food / all_food) * 100:.2f}% of the food has been eaten.')
print(f'{(count_dog_eaten_food / total_eaten_food) * 100:.2f}% eaten from the dog.')
print(f'{(count_cat_eaten_food / total_eaten_food) * 100:.2f}% eaten from the cat.')
