VIP_TICKET_PRICE = 499.99
NORMAL_TICKET_PRICE = 249.99

budget = float(input())
type_of_ticket = str.lower(input()).strip()
number_of_people = int(input())
transport_price = 0
ticket_price = 0

if number_of_people >= 50:
    transport_price = budget * 0.25
elif number_of_people >= 25:
    transport_price = budget * 0.4
elif number_of_people >= 10:
    transport_price = budget * 0.5
elif number_of_people >= 5:
    transport_price = budget * 0.6
elif number_of_people > 0:
    transport_price = budget * 0.75

if type_of_ticket == 'normal':
    ticket_price = NORMAL_TICKET_PRICE
elif type_of_ticket == 'vip':
    ticket_price = VIP_TICKET_PRICE

total_ticket_price = ticket_price * number_of_people
left_money = budget - transport_price

if left_money >= total_ticket_price:
    print(f"Yes! You have {left_money - total_ticket_price:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_ticket_price - left_money:.2f} leva.")
