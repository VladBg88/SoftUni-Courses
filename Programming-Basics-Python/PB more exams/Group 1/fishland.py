SHELLS_PRICE = 7.50

mackerel_price = float(input())
sprinkle_price = float(input())

palamud_kilograms = float(input())
safrid_kilograms = float(input())
shells_kilograms = int(input())

PALAMUD_PRICE = 1.6 * mackerel_price
SAFRID_PRICE = 1.8 * sprinkle_price

total_price = shells_kilograms * SHELLS_PRICE + safrid_kilograms * SAFRID_PRICE + palamud_kilograms * PALAMUD_PRICE
print(f"{total_price:.2f}")
