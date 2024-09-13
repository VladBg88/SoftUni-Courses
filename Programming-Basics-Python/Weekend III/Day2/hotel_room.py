MAY_OCTOBER_STUDIO = 50
MAY_OCTOBER_APARTMENT = 65
JUNE_SEPTEMBER_STUDIO = 75.20
JUNE_SEPTEMBER_APARTMENT = 68.70
JULY_AUGUST_STUDIO = 76
JULY_AUGUST_APARTMENT = 77

month = str(input())
days = int(input())
studio_price = 0.00
apartment_price = 0.00
studio_discount = 0.00
apartment_discount = 0.00

if month == 'May' or month == 'October':
    if 7 < days <= 14:
        studio_discount = 0.95
if month == 'May' or month == 'October':
    if days > 14:
        studio_discount = 0.70
if month == 'June' or month == 'September':
    if days > 14:
        studio_discount = 0.80

if days > 14:
    apartment_discount = 0.90

if month == 'May' or month == 'October':
    studio_price = MAY_OCTOBER_STUDIO * days
    apartment_price = MAY_OCTOBER_APARTMENT * days
if month == 'June' or month == 'September':
    studio_price = JUNE_SEPTEMBER_STUDIO * days
    apartment_price = JUNE_SEPTEMBER_APARTMENT * days
if month == 'July' or month == 'August':
    studio_price = JULY_AUGUST_STUDIO * days
    apartment_price = JULY_AUGUST_APARTMENT * days

if studio_discount > 0:
    studio_price = studio_price * studio_discount
if apartment_discount > 0:
    apartment_price = apartment_price * apartment_discount

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
