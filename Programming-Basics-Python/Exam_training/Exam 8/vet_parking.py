days = int(input())
hours = int(input())
tax = 0
day_sum = 0

for i in range(days):
    for j in range(hours):
        if (i + 1) % 2 == 0 and (j + 1) % 2 != 0:
            tax += 2.5
            day_sum += 2.5

        elif (i + 1) % 2 != 0 and (j + 1) % 2 == 0:
            tax += 1.25
            day_sum += 1.25
        else:
            tax += 1
            day_sum += 1

    print(f'Day: {i + 1} - {day_sum:.2f} leva')
    day_sum = 0

print(f'Total: {tax:.2f} leva')
