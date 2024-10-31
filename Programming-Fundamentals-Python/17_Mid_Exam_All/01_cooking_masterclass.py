from math import ceil

budget = float(input())
students = int(input())
flour_package_price = float(input())
egg_price = float(input())
apron_price = float(input())
apron_needed = ceil(students * 1.2)
egg_needed = 10 * students
flour_needed = students - (students // 5)

apron_price *= apron_needed
egg_price *= egg_needed
flour_package_price *= flour_needed

total_price = apron_price + egg_price + flour_package_price

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{(total_price - budget):.2f}$ more needed.")
