packages = int(input())
van = 0
truck = 0
train = 0
total_price = 0
total_weight = 0

for i in range(1, packages + 1):
    weight = int(input())
    if weight >= 12:
        train += weight
        total_weight += weight
        total_price += 120 * weight
    elif weight >= 4:
        truck += weight
        total_weight += weight
        total_price += 175 * weight
    elif weight <= 3:
        van += weight
        total_weight += weight
        total_price += 200 * weight

print(f'{total_price / total_weight:.2f}')
print(f'{100 / total_weight * van:.2f}%')
print(f'{100 / total_weight * truck:.2f}%')
print(f'{100 / total_weight * train:.2f}%')
