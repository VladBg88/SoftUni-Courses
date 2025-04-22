season = str(input())
type_of_group = str(input())
number_of_students = int(input())
nights = int(input())

if type_of_group == 'boys' or type_of_group == 'girls':
    if season == 'Winter':
        price = 9.60
    elif season == 'Spring':
        price = 7.20
    elif season == 'Summer':
        price = 15
elif type_of_group == 'mixed':
    if season == 'Winter':
        price = 10
    elif season == 'Spring':
        price = 9.50
    elif season == 'Summer':
        price = 20

if number_of_students >= 50:
    price *= 0.5
elif number_of_students >= 20:
    price *= 0.85
elif number_of_students >= 10:
    price *= 0.95

if type_of_group == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    elif season == 'Summer':
        sport = 'Volleyball'
elif type_of_group == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    elif season == 'Summer':
        sport = 'Football'
elif type_of_group == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    elif season == 'Summer':
        sport = 'Swimming'

print(f'{sport} {price * nights * number_of_students:.2f} lv.')
