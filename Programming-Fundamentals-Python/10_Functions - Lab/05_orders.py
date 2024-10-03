def orders(product, quantity):
    if product == "coffee":
        return quantity * 1.50
    elif product == "water":
        return quantity * 1.00
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2.00


user_product = input().strip()
user_quantity = int(input())
result = orders(user_product, user_quantity)
print("{:.2f}".format(result))
