price_without_taxes = 0
taxes = 0

while True:
    command = input()
    if command == 'regular':
        break
    elif command == 'special':
        break

    if float(command) < 0:
        print("Invalid price!")
        continue

    price_without_taxes += float(command)


if price_without_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {((price_without_taxes * 1.2) - price_without_taxes):.2f}$")
    print("-----------")
    if command == 'special':
        print(f"Total price: {((price_without_taxes * 1.2) * 0.9):.2f}$")
    else:
        print(f"Total price: {(price_without_taxes * 1.2):.2f}$")
