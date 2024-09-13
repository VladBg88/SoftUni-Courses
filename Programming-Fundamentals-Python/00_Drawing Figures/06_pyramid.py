rows = int(input())  #5

for i in range(rows):  #0-4
    print(' ' * (rows - i - 1) + '*' * (i * 2 + 1))
