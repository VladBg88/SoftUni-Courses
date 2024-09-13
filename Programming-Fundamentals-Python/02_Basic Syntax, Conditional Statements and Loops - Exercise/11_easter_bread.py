budget = float(input())
flour_price_per_kg = float(input())
total_loaf_count = 0
colored_eggs = 0

eggs_pack_price = flour_price_per_kg * 0.75
milk_1l_price = flour_price_per_kg * 1.25

loaf_price = flour_price_per_kg + eggs_pack_price + (milk_1l_price * 0.25)

while True:
    if budget > loaf_price:
        budget -= loaf_price
        total_loaf_count += 1
        colored_eggs += 3
    else:
        break

    if total_loaf_count % 3 == 0:
        colored_eggs -= total_loaf_count - 2

print(f"You made {total_loaf_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
