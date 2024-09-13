budget = float(input())
spending = 0
counter_product = 1
total_counter_of_product = 0

while True:
    name_of_product = str(input())
    if name_of_product == 'Stop':
        break
    price_of_product = float(input())

    if counter_product == 3:
        price_of_product /= 2
        counter_product = 0

    if price_of_product + spending > budget:
        print("You don't have enough money!")
        print(f'You need {spending + price_of_product - budget:.2f} leva!')
        exit()

    counter_product += 1
    total_counter_of_product += 1
    spending += price_of_product

print(f'You bought {total_counter_of_product} products for {spending:.2f} leva.')
