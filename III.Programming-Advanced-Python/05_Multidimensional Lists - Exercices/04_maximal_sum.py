rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for repeat in range(rows)]
f_row, f_col = [0, 0]
best_sum = float("-inf")

for i in range(rows - 2):
    for j in range(cols - 2):
        current_sum = sum(matrix[i + x][j + y] for x in range(3) for y in range(3))
        if current_sum > best_sum:
            best_sum = current_sum
            f_row, f_col = [i, j]

print(f"Sum = {best_sum}")
for i in range(3):
    print(*matrix[f_row + i][f_col:f_col + 3])
