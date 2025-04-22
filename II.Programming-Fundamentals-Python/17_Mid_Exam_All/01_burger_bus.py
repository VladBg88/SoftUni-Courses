number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    name_of_city = input()
    earned_money = float(input())
    expenses = float(input())

    if city % 3 == 0 and not city % 5 == 0:
        expenses *= 1.5

    if city % 5 == 0:
        earned_money *= 0.9

    profit = round(earned_money - expenses, 2)
    if profit > 0:
        total_profit += profit
    else:
        total_profit -= abs(profit)

    print(f"In {name_of_city} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
