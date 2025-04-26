rows, cols = [int(x) for x in input().split(', ')]
matrix = []
biggest_submatrix = [0, 0, 0, 0, 0]

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

for row in range(rows - 1):
    for col in range(cols - 1):
        if sum([
                matrix[row][col],
                matrix[row][col + 1],
                matrix[row + 1][col],
                matrix[row + 1][col + 1]
        ]) > biggest_submatrix[-1]:
            biggest_submatrix = [
                matrix[row][col],
                matrix[row][col + 1],
                matrix[row + 1][col],
                matrix[row + 1][col + 1],
                sum([
                    matrix[row][col],
                    matrix[row][col + 1],
                    matrix[row + 1][col],
                    matrix[row + 1][col + 1]
                ])
            ]

print(f"{biggest_submatrix[0]} {biggest_submatrix[1]}")
print(f"{biggest_submatrix[2]} {biggest_submatrix[3]}")
print(biggest_submatrix[-1])