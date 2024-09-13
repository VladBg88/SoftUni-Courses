ROOM_FOR_ONE_PERSON = 18.00
APARTMENT = 25.00
PRESIDENT_APARTMENT = 35.00

days = int(input())
type_of_room = str(input())
rating = str(input())

discount = 0.00
price = 0.00
total_price = 0.00

if type_of_room == 'apartment':
    if days < 10:
        discount = 0.70
    if 10 <= days <= 15:
        discount = 0.65
    if days > 15:
        discount = 0.50

if type_of_room == 'president apartment':
    if days < 10:
        discount = 0.90
    if 10 <= days <= 15:
        discount = 0.85
    if days > 15:
        discount = 0.80

if type_of_room == 'room for one person':
    price = (days - 1) * ROOM_FOR_ONE_PERSON
if type_of_room == 'apartment':
    price = (days - 1) * APARTMENT * discount
if type_of_room == 'president apartment':
    price = (days - 1) * PRESIDENT_APARTMENT * discount

if rating == 'positive':
    total_price = price * 1.25
if rating == 'negative':
    total_price = price * 0.9

print(f'{total_price:.2f}')
