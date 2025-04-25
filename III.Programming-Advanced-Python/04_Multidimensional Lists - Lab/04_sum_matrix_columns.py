rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for row in range(rows)]
sum_columns = []

column_sums = list(map(sum, zip(*matrix)))

for num in column_sums:
    print(num)
