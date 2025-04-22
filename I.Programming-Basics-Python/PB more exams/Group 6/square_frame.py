n = int(input())

for i in range(n):
    if i == 0:
        print('+' + ((n - 2) * ' -') + ' +')
        continue
    if i == n - 1:
        print('+' + ((n - 2) * ' -') + ' +')
        continue

    print('|' + ((n - 2) * ' -') + ' |')
