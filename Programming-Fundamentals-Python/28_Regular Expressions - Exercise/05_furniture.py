import re
bought_furniture = []
total_price = 0

while True:
    command = input()
    if command == "Purchase":
        break

    pattern = r">>(?P<product>[A-za-z]+)<<(?P<price>([\d]+)\.?([\d]+)?)\!(?P<quantity>[\d]+)"
    matches = re.finditer(pattern, command)

    for match in matches:
        product = match.group('product')
        price = float(match.group('price'))
        quantity = int(match.group('quantity'))
        total_price += price * quantity
        bought_furniture.append(product)

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")