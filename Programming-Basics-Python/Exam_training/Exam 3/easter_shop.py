eggs_reserve = int(input())
sold_eggs = 0

while True:
    command = input()
    if command == 'Close':
        break
    number = int(input())

    if command == 'Buy' and number > eggs_reserve:
        print('Not enough eggs in store!')
        print(f'You can buy only {eggs_reserve}.')
        break

    if command == 'Buy':
        eggs_reserve -= number
        sold_eggs += number
    elif command == 'Fill':
        eggs_reserve += number

if command == 'Close':
    print('Store is closed!')
    print(f'{sold_eggs} eggs sold.')
