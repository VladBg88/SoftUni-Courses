rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)
