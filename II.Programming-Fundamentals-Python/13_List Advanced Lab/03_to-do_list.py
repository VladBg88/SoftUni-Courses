def to_do_list():
    to_do = [0] * 10
    command = input()
    while command != 'End':
        command = command.split('-')
        priority = int(command[0]) - 1
        note = command[1]
        to_do.pop(priority)
        to_do.insert(priority, note)

        command = input()

    result = [element for element in to_do if element != 0]
    print(result)


to_do_list()
