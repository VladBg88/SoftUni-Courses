from collections import deque


clothes = deque([int(x) for x in input().split()])
rack_capacity = int(input())
rack_counter = 0

while clothes:
    current_rack_capacity = rack_capacity
    rack_counter += 1
    while clothes and clothes[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes.pop()
    else:
        continue

print(rack_counter)

