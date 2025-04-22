items_and_prices = input().split('|')
budget = float(input())
profit = 0
clothes_max = 50.00
shoes_max = 35.00
accessories_max = 20.50
train_ticket = 150
markup = 1.4
bought_items_list = []
second_budget = 0

for i in range(len(items_and_prices)):
    product_details = items_and_prices[i].split('->')
    if product_details[0] == "Clothes" and float(product_details[1]) <= clothes_max:
        if float(product_details[1]) <= budget:
            budget -= float(product_details[1])
            profit += (float(product_details[1]) * markup) - float(product_details[1])
            bought_items_list.append(f'{(float(product_details[1]) * markup):.2f}')
            second_budget += float(product_details[1]) * markup
    elif product_details[0] == "Shoes" and float(product_details[1]) <= shoes_max:
        if float(product_details[1]) <= budget:
            budget -= float(product_details[1])
            profit += (float(product_details[1]) * markup) - float(product_details[1])
            bought_items_list.append(f'{(float(product_details[1]) * markup):.2f}')
            second_budget += float(product_details[1]) * markup
    elif product_details[0] == "Accessories" and float(product_details[1]) <= accessories_max:
        if float(product_details[1]) <= budget:
            budget -= float(product_details[1])
            profit += (float(product_details[1]) * markup) - float(product_details[1])
            bought_items_list.append(f'{(float(product_details[1]) * markup):.2f}')
            second_budget += float(product_details[1]) * markup

budget += second_budget
print(*bought_items_list)
print(f'Profit: {profit:.2f}')
if budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
