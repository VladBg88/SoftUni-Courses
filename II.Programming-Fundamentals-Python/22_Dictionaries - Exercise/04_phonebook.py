phonebook_dict = {}

while True:
    command = input()
    if '-' in command:
        command = command.split('-')
        name, phone = command[0], command[1]
        phonebook_dict[name] = phone
        continue

    for n in range(int(command)):
        search_name = input()
        if search_name in phonebook_dict:
            print(f'{search_name} -> {phonebook_dict[search_name]}')
        else:
            print(f"Contact {search_name} does not exist.")

    break
