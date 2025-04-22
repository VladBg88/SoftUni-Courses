import math

MAGNOLII = 3.25
ZIUMBIULI = 4
ROSES = 3.50
CACTUS = 8

magnolii_num = int(input())
ziumbiuli_num = int(input())
roses_num = int(input())
cactus_num = int(input())
price_for_gift = float(input())

total1 = magnolii_num * MAGNOLII + ziumbiuli_num * ZIUMBIULI
total2 = roses_num * ROSES + cactus_num * CACTUS
final_total = (total1 + total2) * 0.95

if final_total >= price_for_gift:
    print(f"She is left with {math.floor(final_total - price_for_gift)} leva.")
else:
    print(f"She will have to borrow {math.ceil(price_for_gift - final_total)} leva.")
