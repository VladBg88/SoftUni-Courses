import math

people_number = int(input())
tax_entry = float(input())
price_sun_lounger = float(input())
price_umbrella = float(input())

total_tax_entry = people_number * tax_entry
total_price_sun_lounger1 = math.ceil(people_number * 0.75)
total_price_sun_lounger2 = total_price_sun_lounger1 * price_sun_lounger
total_umbrella_price1 = math.ceil(people_number * 0.5)
total_umbrella_price2 = total_umbrella_price1 * price_umbrella

total_price = total_umbrella_price2 + total_price_sun_lounger2 + total_tax_entry

print(f'{total_price:.2f} lv.')
