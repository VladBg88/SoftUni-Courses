products_storage = {}

while True:
    user_input = input().split()
    if user_input[0] == 'buy':
        break
    product, price, quantity = user_input[0], float(user_input[1]), int(user_input[2])

    if product not in products_storage:
        products_storage[product] = {}
        products_storage[product]["price"] = price
        products_storage[product]["quantity"] = quantity
    else:
        products_storage[product]['quantity'] += quantity
        products_storage[product]['price'] = price

for product, details in products_storage.items():
    price = products_storage[product]['price']
    quantity = products_storage[product]['quantity']
    total_price = (price * quantity)
    print(f"{product} -> {total_price:.2f}")
