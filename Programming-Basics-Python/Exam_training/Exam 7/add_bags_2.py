bag_price_over_20kg = float(input())
bag_kilograms = float(input())
days_until_travel = int(input())
number_of_bags = int(input())
extra_charge = 1

if 0 <= bag_kilograms < 10:
    bag_price_over_20kg *= 0.2
elif bag_kilograms <= 20:
    bag_price_over_20kg *= 0.5

if 0 <= days_until_travel < 7:
    extra_charge = 1.4
elif days_until_travel <= 30:
    extra_charge = 1.15
elif days_until_travel > 30:
    extra_charge = 1.1

total_price = bag_price_over_20kg * number_of_bags * extra_charge
print(f'The total price of bags is: {total_price:.2f} lv.')