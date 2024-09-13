bag_price_over_20kg = float(input())
bag_kilograms = float(input())
days_until_travel = int(input())
number_of_bags = int(input())
extra_charge = 0

if bag_kilograms > 20:
    tax_price = bag_price_over_20kg
elif bag_kilograms > 9:
    tax_price = 0.5 * bag_price_over_20kg
elif bag_kilograms > 0:
    tax_price = 0.2 * bag_price_over_20kg
else:
    tax_price = 0

if days_until_travel > 30:
    extra_charge = 1.1
elif days_until_travel > 6:
    extra_charge = 1.15
else:
    extra_charge = 1.4

total_price = tax_price * number_of_bags * extra_charge
print(f'The total price of bags is: {total_price:.2f} lv.')
