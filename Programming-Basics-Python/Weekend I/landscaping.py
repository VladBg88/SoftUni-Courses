area = float(input())
price_per_square_meter = 7.61

total_price = area * price_per_square_meter
discount = 18 / 100 * total_price
final_price = total_price - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
