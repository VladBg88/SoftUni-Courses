men = int(input())
women = int(input())
max_number_tables = int(input())

for i in range(1, men + 1):
    for k in range(1, women + 1):
        if max_number_tables == 0:
            break

        print(f'({i} <-> {k})', end=' ')
        max_number_tables -= 1
