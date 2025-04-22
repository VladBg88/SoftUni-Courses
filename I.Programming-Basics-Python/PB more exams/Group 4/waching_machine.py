PLATE = 5
POT = 15
counter = 1
plates_counter = 0
pots_counter = 0

number_of_bottles = int(input())
detergent = number_of_bottles * 750
used_detergent = 0

while True:
    dishes = input()
    if dishes == 'End':
        break

    if counter % 3 == 0:
        needed_detergent = int(dishes) * POT
        pots_counter += int(dishes)
    else:
        needed_detergent = int(dishes) * PLATE
        plates_counter += int(dishes)

    if needed_detergent + used_detergent > detergent:
        print(f'Not enough detergent, {(used_detergent + needed_detergent) - detergent} ml. more necessary!')
        exit()

    used_detergent += needed_detergent
    counter += 1


print('Detergent was enough!')
print(f'{plates_counter} dishes and {pots_counter} pots were washed.')
print(f'Leftover detergent {detergent - used_detergent} ml.')
