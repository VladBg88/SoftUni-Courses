rows_index, col_index = [int(x) for x in input().split(', ')]
total_sum = 0
matrix = []

for i in range(rows_index):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)
    total_sum += sum(line)

print(total_sum)
print(matrix)


