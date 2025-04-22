WATER_TAX = 20
INTERNET_TAX = 15
electricity_total_taxes = 0

months = int(input())

water_total_taxes = WATER_TAX * months
internet_total_taxes = INTERNET_TAX * months
other_total_taxes = 0

for i in range(1, months + 1):
    electricity_tax = float(input())
    electricity_total_taxes += electricity_tax
    other_taxes = (electricity_tax + WATER_TAX + INTERNET_TAX) * 1.2
    other_total_taxes += other_taxes

all_taxes = water_total_taxes + internet_total_taxes + other_total_taxes + electricity_total_taxes

print(f'Electricity: {electricity_total_taxes:.2f} lv')
print(f'Water: {water_total_taxes:.2f} lv')
print(f'Internet: {internet_total_taxes:.2f} lv')
print(f'Other: {other_total_taxes:.2f} lv')
print(f'Average: {all_taxes / months:.2f} lv')
