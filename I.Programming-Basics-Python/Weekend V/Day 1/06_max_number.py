import sys

b = sys.maxsize
a = input()

while a != "Stop":
    if int(a) < b:
        b = int(a)
    a = input()

print(b)
