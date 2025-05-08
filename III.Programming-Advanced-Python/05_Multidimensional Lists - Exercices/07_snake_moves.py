from collections import deque

rows, cols = [int(x) for x in input().split()]
snake = input()
matrix = [[[] for col in range(cols)] for row in range(rows)]
snake_moves = deque(snake)
row, col = [0, 0]

while row != rows:
    while col != cols:
        if snake_moves:
            if row % 2 == 0 or row == 0:
                matrix[row][col] = snake_moves.popleft()
            else:
                matrix[row][-1 - col] = snake_moves.popleft()
        else:
            snake_moves = deque(snake)
            col -= 1
        col += 1
    row += 1
    col = 0


for row in matrix:
    print(''.join(map(str, row)))
