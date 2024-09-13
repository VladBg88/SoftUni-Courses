username = input()
password = input()

login_password = input()

while True:
    if password == login_password:
        print(f"Welcome {username}!")
        break

    login_password = input()
