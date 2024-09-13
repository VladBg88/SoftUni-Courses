n = int(input())
a = '*'
for row in range(1, n + 1):
    print((n - row) * ' ' + a)
    a += ' *'

for row in range(1, n):
    a = ' *' * (n - 1)
    print((row - 1) * ' ' + a)
    n -= 1
