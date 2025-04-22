from collections import deque

total_honey = 0

bees = deque(map(int, input().split()))
nectar = deque(map(int, input().split()))
process = deque(input().split())

while bees and nectar:

    if nectar[-1] < bees[0]:
        nectar.pop()
        continue

    if not nectar:
        break

    symbol = process[0]

    if symbol == '/':
        if nectar[-1] != 0:
            total_honey += abs(bees[0] / nectar[-1])
    elif symbol == '+':
        total_honey += abs(bees[0] + nectar[-1])
    elif symbol == '-':
        total_honey += abs(bees[0] - nectar[-1])
    elif symbol == '*':
        total_honey += abs(bees[0] * nectar[-1])

    bees.popleft()
    nectar.pop()
    process.popleft()


print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
