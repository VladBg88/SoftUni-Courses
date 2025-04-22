import math

number = int(input())
prime = True

for i in range(2, int(math.sqrt(number) + 1)):
    if number % i == 0:
        prime = False
        break

if prime:
    print(prime)
else:
    print(prime)
