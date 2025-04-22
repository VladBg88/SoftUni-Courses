BASKET_PRICE = 1.50
WREATH_PRICE = 3.80
CHOCOLATE_BUNNY_PRICE = 7
count_items = 0
client_total_sum = 0
average_bill = 0

clients_in_the_shop = int(input())

for _ in range(clients_in_the_shop):
    while True:
        purchase = input()
        if purchase == "Finish":
            break

        count_items += 1
        if purchase == 'basket':
            client_total_sum += BASKET_PRICE
        elif purchase == 'wreath':
            client_total_sum += WREATH_PRICE
        elif purchase == 'chocolate bunny':
            client_total_sum += CHOCOLATE_BUNNY_PRICE

    if count_items % 2 == 0:
        print(f'You purchased {count_items} items for {client_total_sum * 0.8:.2f} leva.')
        average_bill += client_total_sum * 0.8
    else:
        print(f'You purchased {count_items} items for {client_total_sum:.2f} leva.')
        average_bill += client_total_sum

    client_total_sum = 0
    count_items = 0

print(f'Average bill per client is: {average_bill / clients_in_the_shop:.2f} leva.')
