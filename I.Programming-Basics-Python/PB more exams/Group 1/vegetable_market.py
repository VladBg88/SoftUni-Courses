price_kg_vegetables = float(input())
price_kg_fruits = float(input())
vegetables_kilograms = int(input())
fruits_kilograms = int(input())

total_price = ((price_kg_vegetables * vegetables_kilograms) + (price_kg_fruits * fruits_kilograms)) / 1.94
print(f"{total_price:.2f}")
