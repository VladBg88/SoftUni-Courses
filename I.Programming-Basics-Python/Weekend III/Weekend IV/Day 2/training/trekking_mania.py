groups_number = int(input())

count_musala = 0
count_monblan = 0
count_kilimandzaro = 0
count_k2 = 0
count_everest = 0
total_count = 0

for _ in range(groups_number):
    people_number = int(input())
    if people_number < 6:
        count_musala += people_number
    elif people_number < 13:
        count_monblan += people_number
    elif people_number < 26:
        count_kilimandzaro += people_number
    elif people_number < 41:
        count_k2 += people_number
    else:
        count_everest += people_number

total_count = count_musala + count_monblan + count_kilimandzaro + count_k2 + count_everest

print(f'{count_musala / total_count * 100:.2f}%')
print(f'{count_monblan / total_count * 100:.2f}%')
print(f'{count_kilimandzaro / total_count * 100:.2f}%')
print(f'{count_k2 / total_count * 100:.2f}%')
print(f'{count_everest / total_count * 100:.2f}%')
