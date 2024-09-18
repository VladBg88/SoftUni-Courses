import time


def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Move to the next line after printing the string


# Usage
slow_print("Choose a data type to perform operations on:", delay=0.1)

print(f" 1. Strings \n 2. Numbers \n 3. Booleans \n 4. Additional Data Types (List, Tuple, Dictionary)")
command = input("\nEnter the number of your choice (1-4):  ")

while True:
    if command in ['1', '2', '3', '4']:
        break
    if command not in ['1', '2', '3', '4']:
        print('Wrong input! Please try again.')
        command = input("\nEnter the number of your choice (1-4):  ")

if command == '1':
    slow_print("\nChoose an operation from Strings:", delay=0.1)
    print("1. Declare a string variable.")
    print("2. Extract and print a substring.")
    print("3. Convert the entire sentence to uppercase or lowercase and print it.")
    print('4. Replace a word in the sentence and print the modified sent.')

    string_command = input("\nEnter the number of your choice (1-4):  ")

    while True:
        if string_command in ['1', '2', '3', '4']:
            break
        if string_command not in ['1', '2', '3', '4']:
            print('Wrong input! Please try again.')
            string_command = input("\nEnter the number of your choice (1-4):  ")

    if string_command == '1':
        string_command = input("Enter your string: ")
        print(string_command)






elif command == '2':
    slow_print("Choose an operation from Numbers:", delay=0.1)
    print('Prompt the user to input ')