def password_manager():

    password = input()

    while True:
        command = input()
        if command == "Complete":
            break

        parts = command.split()
        action = parts[0]

        if action == "Make":

            case = parts[1]
            index = int(parts[2])
            if case == "Upper":
                password = password[:index] + password[index].upper() + password[index + 1:]
            elif case == "Lower":
                password = password[:index] + password[index].lower() + password[index + 1:]
            print(password)

        elif action == "Insert":

            index = int(parts[1])
            char = parts[2]
            if 0 <= index <= len(password):
                password = password[:index] + char + password[index:]
            print(password)

        elif action == "Replace":

            char = parts[1]
            value = int(parts[2])
            if char in password:
                new_char = chr(ord(char) + value)
                password = password.replace(char, new_char)
            print(password)

        elif action == "Validation":

            valid = True
            if len(password) < 8:
                print("Password must be at least 8 characters long!")
                valid = False
            if not (all(c.isalpha() or c.isdigit() or c == "_" for c in password)):
                print("Password must consist only of letters, digits and _!")
                valid = False
            if not any(c.isupper() for c in password):
                print("Password must consist at least one uppercase letter!")
                valid = False
            if not any(c.islower() for c in password):
                print("Password must consist at least one lowercase letter!")
                valid = False
            if not any(c.isdigit() for c in password):
                print("Password must consist at least one digit!")
                valid = False


password_manager()