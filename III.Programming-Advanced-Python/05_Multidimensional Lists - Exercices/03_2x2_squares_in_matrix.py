row, col = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for symbols in range(row)]
counter = 0

for i in range(row - 1):
    for j in range(col - 1):
        a, b = matrix[i][j:j+2]
        c, d = matrix[i + 1][j:j+2]
        if a == b and b == c and c == d:
            counter += 1

print(counter)
