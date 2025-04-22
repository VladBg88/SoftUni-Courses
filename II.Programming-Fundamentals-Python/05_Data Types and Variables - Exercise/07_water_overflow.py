water_tank_capacity = 255
pouring_times = int(input())
liters_in_tank = 0

for i in range(pouring_times):
    command = int(input())

    if liters_in_tank + command > water_tank_capacity:
        print('Insufficient capacity!')
        continue

    liters_in_tank += command

print(liters_in_tank)
