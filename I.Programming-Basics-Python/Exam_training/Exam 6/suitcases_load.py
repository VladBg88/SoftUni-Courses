storage_capacity = float(input())
filled_space = 0
counter_suitcases = 1

while True:
    suitcase_size = input()
    if suitcase_size == 'End':
        print(f'Congratulations! All suitcases are loaded!')
        break

    if counter_suitcases % 3 == 0:
        suitcase_size = 1.1 * float(suitcase_size)

    if filled_space + float(suitcase_size) > storage_capacity:
        print(f'No more space!')
        break

    filled_space += float(suitcase_size)
    counter_suitcases += 1

print(f'Statistic: {counter_suitcases - 1} suitcases loaded.')
