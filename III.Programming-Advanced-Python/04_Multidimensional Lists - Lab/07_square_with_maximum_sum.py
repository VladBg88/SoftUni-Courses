rows, cols = [int(x) for x in input().split(', ')]
best_submatrix = [0, 0, 0, 0]
best_sum = float('-inf')
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

for row in range(rows - 1):
    for col in range(cols - 1):
        current_submatrix = [
                matrix[row][col : col + 2],
                matrix[row + 1][col : col + 2],
            ]
        current_sum = sum(sum(x) for x in current_submatrix)
        if current_sum > best_sum:
            best_submatrix, best_sum = current_submatrix, current_sum

for nums in best_submatrix:
    print(*nums)
print(best_sum)

