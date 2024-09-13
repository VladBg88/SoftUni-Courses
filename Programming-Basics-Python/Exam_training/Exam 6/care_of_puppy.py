food_bought = int(input()) * 1000
consumed_food = 0

while True:
    portion = input()
    if portion == 'Adopted':
        break

    consumed_food += int(portion)

if consumed_food <= food_bought:
    print(f'Food is enough! Leftovers: {food_bought - consumed_food} grams.')
else:
    print(f'Food is not enough. You need {consumed_food - food_bought} grams more.')
