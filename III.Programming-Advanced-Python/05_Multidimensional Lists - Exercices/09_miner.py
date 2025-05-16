##    * - a regular position on the field
##    e - the end of the route
##    c - coal
##    s - miner
from collections import deque
size_matrix = int(input())
commands = deque(x for x in input().split())
matrix = [[x for x in input().split()] for y in range(size_matrix)]
collected_coal = 0
current_coal = sum(row.count('c') for row in matrix)
miner_location = next(
    ({"row": r, "col": c} for r, row in enumerate(matrix)
     for c, col in enumerate(row) if col == 's'),
    None
)

while commands:

    move = commands.popleft()
    if move == 'up':
        try:
            if miner_location["row"] > 0:
                miner_location["row"] -= 1
        except IndexError:
            continue
    elif move == 'right':
        try:
            if miner_location["col"] < size_matrix - 1:
                miner_location["col"] += 1
        except IndexError:
            continue
    elif move == 'left':
        try:
            if miner_location["col"] > 0:
                miner_location["col"] -= 1
        except IndexError:
            continue
    elif move == 'down':
        try:
            if miner_location["row"] < size_matrix - 1:
                miner_location["row"] += 1
        except IndexError:
            continue

    if matrix[miner_location["row"]][miner_location["col"]] == 'e':
        print(f"Game over! ({miner_location["row"]}, {miner_location["col"]})")
        exit()
    elif matrix[miner_location["row"]][miner_location["col"]] == 'c':
        matrix[miner_location["row"]][miner_location["col"]] = '*'
        current_coal -= 1
        collected_coal += 1

    if current_coal == 0:
        print(f"You collected all coal! ({miner_location["row"]}, {miner_location["col"]})")
        exit()


print(f"{current_coal} pieces of coal left. ({miner_location["row"]}, {miner_location["col"]})")

