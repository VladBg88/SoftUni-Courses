restaurant_tax = float(input())

cake_price = restaurant_tax * 0.2
drinks_price = cake_price * 0.55
animator_price = restaurant_tax / 3
total_price = restaurant_tax + cake_price + drinks_price + animator_price

print(f'{total_price:.1f}')