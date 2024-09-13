required_money = int(input())
counter = 0
paid_by_cash = 0
paid_by_card = 0
total_sum = 0
count_cash = 0
count_card = 0

while True:
    counter += 1
    price_of_item = input()
    if price_of_item == 'End':
        print('Failed to collect required money for charity.')
        break

    if counter % 2 == 1:
        if int(price_of_item) > 100:
            print('Error in transaction!')
            continue
        else:
            paid_by_cash += int(price_of_item)
            total_sum += int(price_of_item)
            count_cash += 1
            print('Product sold!')
    else:
        if int(price_of_item) < 10:
            print('Error in transaction!')
            continue
        else:
            paid_by_card += int(price_of_item)
            total_sum += int(price_of_item)
            count_card += 1
            print('Product sold!')

    if total_sum >= required_money:
        print(f'Average CS: {paid_by_cash / count_cash:.2f}')
        print(f'Average CC: {paid_by_card / count_card:.2f}')
        break
