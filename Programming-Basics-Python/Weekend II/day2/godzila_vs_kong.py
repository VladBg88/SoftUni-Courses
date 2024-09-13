movie_budget = float(input())
people_number = int(input())
price_per_costume = float(input())

movie_decor = movie_budget * 0.1

if people_number > 150:
    price_per_costume = price_per_costume * 0.9

costumes_price = price_per_costume * people_number

if costumes_price + movie_decor > movie_budget:
    more_money = costumes_price + movie_decor - movie_budget
    print("Not enough money!")
    print(f'Wingard needs {more_money:.2f} leva more.')
else:
    left_money = movie_budget - costumes_price - movie_decor
    print("Action!")
    print(f"Wingard starts filming with {left_money:.2f} leva left.")
