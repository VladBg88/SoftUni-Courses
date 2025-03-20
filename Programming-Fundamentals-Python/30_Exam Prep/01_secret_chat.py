concealed_message = input()

while True:
    command = input()
    if command == "Reveal":
        print(f"You have a new text message: {concealed_message}")
        break
    elif command.startswith("InsertSpace:"):
        index = int(command.split(":|:")[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]
        print(concealed_message)
    elif command.startswith("Reverse:"):
        substring = command.split(":|:")[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print("error")
    elif command.startswith("ChangeAll:"):
        substring, replacement = command.split(":|:")[1], command.split(":|:")[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)