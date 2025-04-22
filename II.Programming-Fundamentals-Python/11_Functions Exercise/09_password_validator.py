def password_validator(password):
    is_valid = True

    if 6 <= len(password) <= 10:
        pass
    else:
        print("Password must be between 6 and 10 characters")
        is_valid = False

    if password.isalnum():
        pass
    else:
        print('Password must consist only of letters and digits')
        is_valid = False

    count_numbers = 0
    for digit in password:
        if digit.isnumeric():
            count_numbers += 1

    if count_numbers >= 2:
        pass
    else:
        print('Password must have at least 2 digits')
        is_valid = False

    return is_valid


password_to_check = input()
is_valid = password_validator(password_to_check)

if is_valid:
    print('Password is valid')
