flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_packs = int(input())
yeast_packs = int(input())

sugar_price = flour_price * 0.75
eggs_price = flour_price * 1.1
yeast_price = sugar_price * 0.2

total_price = flour_price * flour_kg + sugar_price * sugar_kg + eggs_price * eggs_packs + yeast_price * yeast_packs
print(f"{total_price:.2f}")
