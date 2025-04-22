import sys

num_count = int(input())
num_sum = 0
max_number = -sys.maxsize

for _ in range(num_count):
    cur_number = int(input())

    num_sum += cur_number

    if cur_number > max_number:
        max_number = cur_number

if num_sum / 2 == max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (num_sum - max_number))}")
