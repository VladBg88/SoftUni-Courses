password = input().strip()

while True:
    command = input()
    if command == 'Done':
        print(f"Your password is: {password}")
        break

    if command.startswith('TakeOdd'):
        password = ''.join(password[i] for i in range(1, len(password), 2))
        print(password)
    elif command.startswith('Cut'):
        index, length = map(int, command.split()[1:3])
        password = password[:index] + password[index + length:]
        print(password)
    elif command.startswith('Substitute'):
        substring, substitute = command.split()[1:]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')