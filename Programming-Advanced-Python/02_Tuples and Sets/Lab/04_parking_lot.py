cars_num = int(input())
parking_lot = set()

for car in range(cars_num):
    command, number = input().split(', ')
    if command == 'IN':
        if number not in parking_lot:
            parking_lot.add(number)
    elif command == 'OUT':
        if number in parking_lot:
            parking_lot.remove(number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)
