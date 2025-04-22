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
counter_wrong_input_a = 1
counter_wrong_input_b = 1

while True:
    if command in ['1', '2', '3', '4']:
        break
    if command not in ['1', '2', '3', '4']:
        if counter_wrong_input_a % 5 == 0 and counter_wrong_input_a != 0:
            print('Should you call your mom to help you with that extremely tough task?')
            string_command = input("\nEnter the number of your choice (1-4):  ")
            counter_wrong_input_a += 1
            continue
        if counter_wrong_input_a % 3 == 0 and counter_wrong_input_a != 0:
            print("C'mon, bro! Why can't you just pick a simple number between 1 and 4?")
            string_command = input("\nEnter the number of your choice (1-4):  ")
            counter_wrong_input_a += 1
            continue
        print('Wrong input! Please try again.')
        command = input("\nEnter the number of your choice (1-4):  ")
        counter_wrong_input_a += 1

if command == '1':
    slow_print(
        '\nStrings in Python are sequences of characters used to store and manipulate text, and you can perform\n'
        'operations like slicing, concatenation, and various built-in methods to modify or access parts of the '
        'text.', delay=0.1)
    string = 'Strings in Python are sequences of characters used to store and manipulate text, and you can perform'
    'operations like slicing, concatenation, and various built-in methods to modify or access parts of the'
    'text.'

    sliced_string = string.split(' ')

    print("\nChoose an operation from Strings:")
    print("1. Extract and print a substring.")
    print("2. ")
    print("3. Convert the entire sentence to uppercase or lowercase and print it.")
    print('4. Replace a word in the sentence and print the modified sent.')

    string_command = input("\nEnter the number of your choice (1-4):  ")

    while True:
        if string_command in ['1', '2', '3', '4']:
            break
        if string_command not in ['1', '2', '3', '4']:
            if counter_wrong_input_b % 5 == 0 and counter_wrong_input_b != 0:
                print('Should you call your mom to help you with that extremely tough task?')
                string_command = input("\nEnter the number of your choice (1-4):  ")
                counter_wrong_input_b += 1
                continue
            if counter_wrong_input_b % 3 == 0 and counter_wrong_input_b != 0:
                print("C'mon, bro! Why can't you just pick a simple number between 1 and 4?")
                string_command = input("\nEnter the number of your choice (1-4):  ")
                counter_wrong_input_b += 1
                continue
            print('Wrong input! Please try again.')
            string_command = input("\nEnter the number of your choice (1-4):  ")
            counter_wrong_input_b += 1

    if string_command == '1':
        string_command = input("Type a word from the description of Python strings to extract: ")
        string_to_extract = input('word: ')






elif command == '2':
    slow_print("Choose an operation from Numbers:", delay=0.1)
    print('Prompt the user to input ')
