from collections import deque

water_reservoir = int(input())
queue = deque()


while True:
    command = input()
    if command == 'Start':
        break

    queue.append(command)

while True:
    command = input()
    if command == 'End':
        break
    if 'refill' in command:
        command = command.split()
        water_reservoir += int(command[1])
    else:
        if int(command) <= water_reservoir:
            print(f"{queue[0]} got water")
            queue.popleft()
            water_reservoir -= int(command)
        else:
            print(f"{queue[0]} must wait")
            queue.popleft()

print(f"{water_reservoir} liters left")