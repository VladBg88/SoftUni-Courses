rows = int(input('How many rows? '))

for i in range(rows + 1):
    for j in range(i):
        print('*', end='')
    print()
