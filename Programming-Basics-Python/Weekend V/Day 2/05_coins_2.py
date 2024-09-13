coins = float(input())
counter_coins = 0

while coins > 0:
    if coins >= 2:
        counter_coins += coins // 2
        coins -= 2 * (coins // 2)

    if coins >= 1:
        counter_coins += 1
        coins = round(coins - 1, 2)

    if coins >= 0.50:
        counter_coins += 1
        coins = round(coins - 0.50, 2)

    if coins >= 0.20:
        if coins >= 0.40:
            counter_coins += 2
            coins = round(coins - 0.40, 2)

    if coins >= 0.20:
        coins = round(coins - 0.20, 2)
        counter_coins += 1

    if coins >= 0.10:
        coins = round(coins - 0.10, 2)
        counter_coins += 1

    if coins >= 0.05:
        coins = round(coins - 0.05, 2)
        counter_coins += 1

    if coins >= 0.02:
        if coins == 0.4:
            coins = round(coins - 0.4, 2)
            counter_coins += 2

    if coins >= 0.02:
        coins = round(coins - 0.02, 2)
        counter_coins += 1

    if coins == 0.01:
        coins = round(coins - 0.01, 2)
        counter_coins += 1

print(int(counter_coins))
