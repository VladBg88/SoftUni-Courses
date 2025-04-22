capacity_of_stadium = int(input())
total_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for i in range(1, total_fans + 1):
    sector = str(input())

    if sector == 'A':
        sector_a += 1
    elif sector == 'B':
        sector_b += 1
    elif sector == 'V':
        sector_v += 1
    elif sector == 'G':
        sector_g += 1

percent = 100 / total_fans

print(f'{percent * sector_a:.2f}%')
print(f'{percent * sector_b:.2f}%')
print(f'{percent * sector_v:.2f}%')
print(f'{percent * sector_g:.2f}%')
print(f'{100 / capacity_of_stadium * total_fans:.2f}%')
