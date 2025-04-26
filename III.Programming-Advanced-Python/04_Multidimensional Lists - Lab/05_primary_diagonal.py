matrix_size = int(input())
matrix = []
sum_diagonal = 0
j = 0

for _ in range(matrix_size):
    matrix.append([int(x) for x in input().split()])

for i in range(matrix_size):

    sum_diagonal += matrix[i][j]
    j += 1

print(sum_diagonal)