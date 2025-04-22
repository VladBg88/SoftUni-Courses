# rest-2|order-10|eggs-100|rest-10

initial_energy = 100
initial_coins = 100
events = input().split('|')

for i in range(len(events)):
    process = events[i].split('-')
    if process[0] == 'rest':
        old_initial_energy = initial_energy
        initial_energy += int(process[1])
        if initial_energy > 100:
            initial_energy = 100
        print(f'You gained {initial_energy - old_initial_energy} energy.')
        print(f'Current energy: {initial_energy}.')
    elif process[0] == 'order':
        if initial_energy >= 30:
            initial_coins += int(process[1])
            initial_energy -= 30
            print(f'You earned {process[1]} coins.')
        else:
            print('You had to rest!')
            initial_energy += 50
            if initial_energy > 100:
                initial_energy = 100
    else:
        if int(process[1]) <= initial_coins:
            initial_coins -= int(process[1])
            print(f'You bought {process[0]}.')
        else:
            print(f'Closed! Cannot afford {process[0]}.')
            break

    if i == (len(events) - 1):
        print('Day completed!')
        print(f'Coins: {initial_coins}')
        print(f'Energy: {initial_energy}')
