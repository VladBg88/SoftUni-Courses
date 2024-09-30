##    High = 89   Low = 28   Medium = 77   Low = 23
data_input = input().split('#')
water_quantity = int(input())
high = [81, 125]
medium = [51, 80]
low = [1, 50]
removed_cells = []
effort_value = 0
total_fire = 0

for i in range(len(data_input)):
    ceil = data_input[i].split(' = ')

    if ceil[0] == 'High':
        if high[0] <= int(ceil[1]) <= high[1]:
            if int(ceil[1]) <= water_quantity:
                water_quantity -=  int(ceil[1])
                removed_cells.append(ceil[1])
                effort_value += float(ceil[1]) * 0.25
                total_fire += int(ceil[1])
        else:
            continue
    elif ceil[0] == 'Medium':
        if medium[0] <= int(ceil[1]) <= medium[1]:
            if int(ceil[1]) <= water_quantity:
                water_quantity -= int(ceil[1])
                removed_cells.append(ceil[1])
                effort_value += float(ceil[1]) * 0.25
                total_fire += int(ceil[1])

        else:
            continue
    elif ceil[0] == 'Low':
        if low[0] <= int(ceil[1]) <= low[1]:
            if int(ceil[1]) <= water_quantity:
                water_quantity -= int(ceil[1])
                removed_cells.append(ceil[1])
                effort_value += float(ceil[1]) * 0.25
                total_fire += int(ceil[1])

print('Cells:')
for i in range(len(removed_cells)):
    print(f' - {removed_cells[i]}')
print(f'Effort: {effort_value:.2f}')
print(f'Total Fire: {total_fire}')
