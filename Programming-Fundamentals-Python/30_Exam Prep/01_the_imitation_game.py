encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        break
    command = command.split("|")
    current_command = command[0]
    if current_command == "Move":
        number_of_letters = int(command[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif current_command == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif current_command == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

print(f"The decrypted message is: {encrypted_message}")