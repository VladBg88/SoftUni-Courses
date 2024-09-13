height = int(input())
second_number = 1

for i in range(1, height + 1, 2):
    print(' ' * (height - second_number - 1) + '*' * i)
    second_number += 1

second_number = height - 3

for j in range(height - 2, 0, -2):
    print(' ' * (height - second_number - 1) + '*' * j)
    second_number -= 1
