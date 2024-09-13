movie_budget = float(input())
people_number = int(input())
clothes_price_per_person = float(input())
decors_price = movie_budget * 0.1

if people_number > 150:
    clothes_price_per_person *= 0.9

total_sum = clothes_price_per_person * people_number + decors_price

if total_sum > movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_sum - movie_budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {movie_budget - total_sum:.2f} leva left.")
