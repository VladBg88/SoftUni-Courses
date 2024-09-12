divisor = int(input())
boundary = int(input())
biggest_number = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i > biggest_number:
            biggest_number = i

print(biggest_number)
