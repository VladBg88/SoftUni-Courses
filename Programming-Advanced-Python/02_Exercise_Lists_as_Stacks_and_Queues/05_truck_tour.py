from collections import deque


pumps_number = int(input())
stops = deque()
index = 0
current_fuel = 0
marker = False

for i in range(pumps_number):
    x, y = map(int, input().split())
    stops.append([x, y])


for j in range(len(stops)):
    if marker:
        break
    petrol = stops[0][0]
    distance = stops[0][1]
    if petrol + current_fuel < distance:
        index += 1
        current_fuel = 0
        stops.rotate(-1)
    else:
        duplicated_stops = deque(stops)
        current_fuel = petrol - distance
        duplicated_stops.rotate(-1)
        for k in range(len(duplicated_stops) - 1):
            petrol = duplicated_stops[0][0]
            distance = duplicated_stops[0][1]
            if petrol + current_fuel < distance:
                break
            else:
                current_fuel = petrol - distance
                duplicated_stops.rotate(-1)
                if k == len(duplicated_stops) - 1:
                    marker = True

            


print(index)