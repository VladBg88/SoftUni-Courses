food_in_kg = float(input())
hay_in_kg = float(input())
cover_in_kg = float(input())
pig_weight_kg = float(input())
enough = True

for day in range(1, 31):
    food_in_kg -= 0.300

    if day % 2 == 0:
        hay_consume = food_in_kg * 0.05
        hay_in_kg -= hay_consume

    if day % 3 == 0:
        cover_consume = pig_weight_kg / 3
        cover_in_kg -= cover_consume

    if food_in_kg <= 0 or hay_in_kg <= 0 or cover_in_kg <= 0:
        enough = False
        break

if enough:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_kg:.2f}, Hay: {hay_in_kg:.2f}, Cover: {cover_in_kg:.2f}.")
else:
    print(f"Merry must go to the pet store!")
