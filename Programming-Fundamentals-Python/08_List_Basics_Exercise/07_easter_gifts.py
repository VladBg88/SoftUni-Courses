names_of_gifts = input().split()

while True:
    command = input()

    if command == 'No Money':
        break

    parts = command.split()

    if 'OutOfStock' in parts[0]:
        to_remove = parts[1]
        for i in range(len(names_of_gifts)):
            if to_remove in names_of_gifts[i]:
                names_of_gifts[i] = 'None'

    if 'Required' in parts[0]:
        if 0 < int(parts[2]) < len(names_of_gifts):
            index = int(parts[2])
            names_of_gifts[index] = parts[1]

    if 'JustInCase' in command:
        names_of_gifts[-1] = parts[1]

names_of_gifts = [gift for gift in names_of_gifts if gift != 'None']
print(" ".join(map(str, names_of_gifts)))
