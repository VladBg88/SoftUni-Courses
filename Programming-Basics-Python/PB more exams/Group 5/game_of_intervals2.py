number_of_pairs = int(input())
result = 0
counter_0_9 = 0
counter_10_19 = 0
counter_20_29 = 0
counter_30_39 = 0
counter_40_50 = 0
counter_invalid = 0

for i in range(1, number_of_pairs + 1):
    a = int(input())

    if 0 <= a <= 9:
        result += a * 0.2
        counter_0_9 += 1
    elif 10 <= a <= 19:
        result += a * 0.3
        counter_10_19 += 1
    elif 20 <= a <= 29:
        result += a * 0.4
        counter_20_29 += 1
    elif 30 <= a <= 39:
        result += 50
        counter_30_39 += 1
    elif 40 <= a <= 50:
        result += 100
        counter_40_50 += 1
    else:
        result /= 2
        counter_invalid += 1

print(f'{result:.2f}')
print(f'From 0 to 9: {((number_of_pairs / 100) * counter_0_9) * 100:.2f}%')
print(f'From 10 to 19: {((number_of_pairs / 100) * counter_10_19) * 100:.2f}%')
print(f'From 20 to 29: {((number_of_pairs / 100) * counter_20_29) * 100:.2f}%')
print(f'From 30 to 39: {((number_of_pairs / 100) * counter_30_39) * 100:.2f}%')
print(f'From 40 to 50: {((number_of_pairs / 100) * counter_40_50) * 100:.2f}%')
print(f'Invalid numbers: {((number_of_pairs / 100) * counter_invalid) * 100:.2f}%')
