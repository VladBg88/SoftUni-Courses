matrix_rows = int(input())
matrix = []

for _ in range(matrix_rows):
    matrix.append([int(i) for i in input().split(', ') if int(i) % 2 == 0])

print(matrix)
