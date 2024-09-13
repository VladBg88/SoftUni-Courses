turns = int(input())
result = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0

for i in range(1, turns + 1):
    number = int(input())
    if number < 0 or number > 50:
        result /= 2
        count6 += 1
        continue

    if number >= 40:
        result += 100
        count5 += 1
    elif number >= 30:
        result += 50
        count4 += 1
    elif number >= 20:
        result += number * 0.4
        count3 += 1
    elif number >= 10:
        result += number * 0.3
        count2 += 1
    elif number >= 0:
        result += number * 0.2
        count1 += 1

percent = 100 / turns
print(f'{result:.2f}')
print(f'From 0 to 9: {count1 * percent:.2f}%')
print(f'From 10 to 19: {count2 * percent:.2f}%')
print(f'From 20 to 29: {count3 * percent:.2f}%')
print(f'From 30 to 39: {count4 * percent:.2f}%')
print(f'From 40 to 50: {count5 * percent:.2f}%')
print(f'Invalid numbers: {count6 * percent:.2f}%')
