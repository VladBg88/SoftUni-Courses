EASTER_BREAD_PRICE = 3.20
EGGS_PRICE = 4.35 / 12
COOKIES_PRICE = 5.40  # PER KILOGRAM
PAINT_FOR_EGGS_PRICE = 0.15  # PER EGG

easter_bread = int(input())
eggs = int(input()) * 12
cookies = int(input())

print(f"{easter_bread * EASTER_BREAD_PRICE + eggs * EGGS_PRICE + cookies * COOKIES_PRICE + PAINT_FOR_EGGS_PRICE * eggs:.2f}")
