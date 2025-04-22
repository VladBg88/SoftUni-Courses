NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
AMB_PRICE = 5.00
NYLON_BUFFER = 2.0
PAINT_BUFFER = 10/100
BAGS_EXPENSES = 0.4

LABOUR_MULTIPLIER = 30/100

nylon = int(input())
paint = int(input())
amb_price = int(input())
hours = int(input())

nylon_total = (nylon + NYLON_BUFFER) * NYLON_PRICE
paint_total = (paint + (paint * PAINT_BUFFER)) * PAINT_PRICE
amb_total = amb_price * AMB_PRICE

total_materials = nylon_total + paint_total + amb_total + BAGS_EXPENSES

price_per_hour = total_materials * LABOUR_MULTIPLIER
total_price_for_labour = hours * price_per_hour

total_price = total_materials + total_price_for_labour

print(total_price)
