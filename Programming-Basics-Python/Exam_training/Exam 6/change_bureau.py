BITCOIN_PRICE = 1168  # BGN
CHINESE_YUAN_PRICE = 0.15  # USD
USD_PRICE = 1.76  # BGN
EURO_PRICE = 1.95  # BGN

bitcoins = int(input())
yuan = float(input())
tax = float(input())

bitcoins_total = (bitcoins * BITCOIN_PRICE) / EURO_PRICE
yuan_to_usd = yuan * CHINESE_YUAN_PRICE
yuan_total = (yuan_to_usd * USD_PRICE) / EURO_PRICE
total_before_tax = bitcoins_total + yuan_total

total_tax = total_before_tax * (tax / 100)
final_total = total_before_tax - total_tax

print(f'{final_total:.2f}')
