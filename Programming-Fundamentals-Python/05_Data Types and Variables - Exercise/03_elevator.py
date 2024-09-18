from math import ceil

persons = int(input())
elevator_capacity = int(input())

result = ceil(persons / elevator_capacity)

print(f'{result}')
