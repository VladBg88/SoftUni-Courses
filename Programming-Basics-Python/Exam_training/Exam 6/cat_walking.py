minutes_walking = int(input())
number_of_walking = int(input())
cat_calories = int(input())

cat_burns = (minutes_walking * 5) * number_of_walking

if cat_burns >= (cat_calories / 2):
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {cat_burns}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {cat_burns}.')
