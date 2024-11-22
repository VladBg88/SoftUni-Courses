number_of_cars = int(input())
all_cars = {}

for number in range(number_of_cars):
    car_info = input().split("|")
    car_type = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])
    all_cars[car_type] = [mileage, fuel]

while True:
    command = input()
    if command == "Stop":
        for car_type, car_info in all_cars.items():
            print(f"{car_type} -> Mileage: {car_info[0]} kms, Fuel in the tank: {car_info[1]} lt.")
        break
    command = command.split(" : ")
    try:
        action, car_type, mileage_to_drive, fuel_to_spend = command[0], command[1], int(command[2]), int(command[3])
    except IndexError:
        action, car_type, fuel_to_spend = command[0], command[1], int(command[2])

    if action == "Drive":
        if all_cars[car_type][1] >= fuel_to_spend:
            all_cars[car_type][0] += mileage_to_drive
            all_cars[car_type][1] -= fuel_to_spend
            print(f"{car_type} driven for {mileage_to_drive} kilometers. {fuel_to_spend} liters of fuel consumed.")
            if all_cars[car_type][0] >= 100000:
                print(f"Time to sell the {car_type}!")
                all_cars.pop(car_type)
        else:
            print("Not enough fuel to make that ride")
    elif action == 'Refuel':
        print(f"{car_type} refueled with {min(fuel_to_spend, 75 - all_cars[car_type][1])} liters")
        all_cars[car_type][1] += fuel_to_spend
        if all_cars[car_type][1] > 75:
            all_cars[car_type][1] = 75
    elif action == 'Revert':
        all_cars[car_type][0] -= int(command[2])
        if all_cars[car_type][0] < 10000:
            all_cars[car_type][0] = 10000
            continue
        print(f"{car_type} mileage decreased by {command[2]} kilometers")

