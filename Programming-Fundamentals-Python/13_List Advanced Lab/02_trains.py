def trains(number_wagons):
    list_wagons = [0 * number_wagons for x in range(number_wagons)]

    command = ''
    while command != ['End']:
        command = input().split()
        if 'add' in command:
            list_wagons[-1] += int(command[1])
        elif 'insert' in command:
            list_wagons[int(command[1])] += int(command[2])
        elif 'leave' in command:
            list_wagons[int(command[1])] -= int(command[2])

    print(list_wagons)


wagons = int(input())
trains(wagons)
