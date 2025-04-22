tax = int(input())

SHOES = 0.6 * tax
CLOTHES = 0.8 * SHOES
BALL = CLOTHES / 4
ACCESSORIES = BALL / 5
total = tax + SHOES + CLOTHES + BALL + ACCESSORIES

print(f"{total:.2f}")
