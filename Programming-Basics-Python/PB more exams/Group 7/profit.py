money_1lv = int(input())
money_2lv = int(input())
money_5lv = int(input())
total_sum = int(input())

for i in range(money_1lv + 1):
    for j in range(money_2lv + 1):
        for k in range(money_5lv + 1):
            if i * 1 + j * 2 + k * 5 == total_sum:
                print(f'{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {total_sum} lv.')
