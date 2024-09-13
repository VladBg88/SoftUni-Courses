strawberries_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberries_price * 0.5
oranges_price = raspberries_price * 0.6
bananas_price = raspberries_price * 0.2

total1 = strawberries_quantity * strawberries_price + bananas_quantity * bananas_price
total2 = oranges_quantity * oranges_price + raspberries_quantity * raspberries_price
final_total = total1 + total2

print(f'{final_total:.2f}')
