BANSKO_PLUS_EQUIPMENT = 100
BANSKO_WITHOUT_EQUIPMENT = 80
VARNA_PLUS_BREAKFAST = 130
VARNA_WITHOUT_BREAKFAST = 100
BANSKO_VIP_PLUS_EQUIPMENT = 0.9
BANSKO_VIP_WITHOUT_EQUIPMENT = 0.95
VARNA_VIP_PLUS_BREAKFAST = 0.88
VARNA_VIP_WITHOUT_BREAKFAST = 0.93

city = str(input())
type_of_packet = str(input())
vip = str(input())
days = int(input())
price = 0

if days < 1:
    print("Days must be positive number!")
    exit()

if city != 'Bansko' and city != 'Borovets' and city != 'Varna' and city != 'Burgas':
    print('Invalid input!')
    exit()

if type_of_packet != "noEquipment" and type_of_packet != "withEquipment" and type_of_packet != "noBreakfast" and type_of_packet != "withBreakfast":
    print('Invalid input!')
    exit()

if city == 'Bansko' or city == "Borovets":
    if type_of_packet == 'withEquipment':
        price = BANSKO_PLUS_EQUIPMENT
        if vip == 'yes':
            price *= BANSKO_VIP_PLUS_EQUIPMENT
    elif type_of_packet == 'noEquipment':
        price = BANSKO_WITHOUT_EQUIPMENT
        if vip == 'yes':
            price *= BANSKO_VIP_WITHOUT_EQUIPMENT
if city == 'Varna' or city == "Burgas":
    if type_of_packet == 'withBreakfast':
        price = VARNA_PLUS_BREAKFAST
        if vip == 'yes':
            price *= VARNA_VIP_PLUS_BREAKFAST
    elif type_of_packet == 'noBreakfast':
        price = VARNA_WITHOUT_BREAKFAST
        if vip == 'yes':
            price *= VARNA_VIP_WITHOUT_BREAKFAST

total_price = days * price
print(f'The price is {total_price:.2f}lv! Have a nice time!')
