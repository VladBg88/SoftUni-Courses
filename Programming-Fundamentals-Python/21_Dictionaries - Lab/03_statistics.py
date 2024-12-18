products = {}
while True:
    command = input()
    if command == 'statistics':
        break
    command = command.split(": ")
    product = command[0]
    quantity = int(command[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity

print("Products in stock:")
for key, value in products.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
