password = input()

while True:
    command = input()
    if command == "Complete":
        break

    elif command.startswith("Make Upper"):
        index = int(command.split()[-1])
        letter = password[index]
        password = password[:index] + letter.upper() + password[index + 1:]
        print(password)
    elif command.startswith("Make Lower"):
        index = int(command.split()[-1])
        letter = password[index]
        password = password[:index] + letter.lower() + password[index + 1:]
        print(password)
    elif command.startswith("Insert"):
        index, letter = command.split()[1:]
        password = password[:int(index)] + letter + password[int(index):]
        print(password)
    elif command.startswith("Replace"):
        character = command.split()[1]
        value = int(command.split()[2])
        final_value = ord(character) + value
        if chr(final_value) in password:
            password = password.replace(chr(final_value), "")
            print(password)
    elif command.startswith("Validation"):
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        check_allowed_symbols = False
        check_one_upper_letter = False
        check_one_lower_letter = False
        check_digits = False
        for char in password:
            if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_":
                check_allowed_symbols = True
            if char.isupper():
                check_one_upper_letter = True
            if char.islower():
                check_one_lower_letter = True
            if char.isdigit():
                check_digits = True

        if check_allowed_symbols:
            print("Password must consist only of letters, digits and _!")
        if check_one_upper_letter:
            print("Password must consist at least one uppercase letter!")
        if check_one_lower_letter:
            print("Password must consist at least one lowercase letter!")

