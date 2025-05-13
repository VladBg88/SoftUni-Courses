matrix = [[int(num) for num in input().split()] for turn in range(int(input()))]
bombs = [[int(num) for num in couples.split(',')] for couples in input().split()]

for coordinates in bombs:
    row, col = coordinates
    bomb_row, bomb_col = coordinates
    if matrix[row][col] <= 0:
        continue
    bomb_power = matrix[row][col]
    matrix[row][col] = 0
    if row > 0:
        row -= 1
    if col > 0:
        col -= 1

    for expl_r in range(3 if bomb_row > 0 else 2):
        for expl_c in range(3 if bomb_col > 0 else 2):
            try:
                if matrix[row + expl_r][col + expl_c] > 0:
                    matrix[row + expl_r][col + expl_c] -= bomb_power
            except IndexError:
                continue

alive_cels = 0
matrix_sum = 0

for line in matrix:
    for num in line:
        if num > 0:
            alive_cels += 1
            matrix_sum += num

print(f"Alive cells: {alive_cels}")
print(f"Sum: {matrix_sum}")
for matrix_line in matrix:
    print(*matrix_line)
    