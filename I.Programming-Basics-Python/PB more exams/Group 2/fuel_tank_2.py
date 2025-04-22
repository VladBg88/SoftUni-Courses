GASOLINE_PRICE = 2.22
DIESEL_PRICE = 2.33
GAS_PRICE = 0.93

type_of_fuel = str.lower(input())
quantity_of_fuel = float(input())
club_card = str.lower(input())
price = 0

if club_card == 'yes':
    GASOLINE_PRICE -= 0.18
    DIESEL_PRICE -= 0.12
    GAS_PRICE -= 0.08

if type_of_fuel == 'diesel':
    price = DIESEL_PRICE
elif type_of_fuel == 'gasoline':
    price = GASOLINE_PRICE
elif type_of_fuel == 'gas':
    price = GAS_PRICE

total1 = price * quantity_of_fuel

if quantity_of_fuel > 25:
    total1 *= 0.9
elif quantity_of_fuel >= 20:
    total1 *= 0.92

print(f"{total1:.2f} lv.")
