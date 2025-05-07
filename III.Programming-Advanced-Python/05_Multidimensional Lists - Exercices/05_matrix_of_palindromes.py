rows, cols = [int(x) for x in input().split()]
matrix = [[chr(97 + i) + chr(97 + j + i) + chr(97+i) for j in range(cols)] for i in range(rows)]
for row in matrix:
    print(' '.join(row))
