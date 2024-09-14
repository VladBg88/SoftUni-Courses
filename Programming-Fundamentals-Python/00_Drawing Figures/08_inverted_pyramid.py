rows = int(input())

for i in range(rows + 1, 1, -1):
    print(' ' * (rows - i + 1) + (i * 2 - 3) * '*')
