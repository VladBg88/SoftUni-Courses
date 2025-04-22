count = int(input())
all_numbers_sum = 0

for i in range(1, count + 1):
    number = int(input())
    all_numbers_sum += number

print(f'{all_numbers_sum / count:.2f}')
