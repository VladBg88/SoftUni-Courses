total_coffees = 0

while True:
    command = input()
    if command == 'END':
        break

    points = 0

    if command == 'coding' or command == 'CODING':
        pass
    elif command == 'dog' or command == 'DOG':
        pass
    elif command == 'cat' or command == 'CAT':
        pass
    elif command == 'movie' or command == 'MOVIE':
        pass
    else:
        continue

    if command.islower():
        points = 1
    else:
        points = 2

    total_coffees += points

if total_coffees <= 5:
    print(total_coffees)
else:
    print(f'You need extra sleep')
