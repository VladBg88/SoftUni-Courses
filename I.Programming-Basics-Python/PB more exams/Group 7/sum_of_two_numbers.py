start_of_interval = int(input())
end_of_interval = int(input())
magical_number = int(input())
counter = 0
end_of_code = False

for i in range(start_of_interval, end_of_interval + 1):
    if end_of_code:
        break
    for j in range(start_of_interval, end_of_interval + 1):
        counter += 1
        if i + j == magical_number:
            print(f'Combination N:{counter} ({i} + {j} = {magical_number})')
            end_of_code = True

if not end_of_code:
    print(f'{counter} combinations - neither equals {magical_number}')
