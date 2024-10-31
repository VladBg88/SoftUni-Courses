secret_message = input().split()
numbers = ''
characters = ''
final_message = ''

for word in secret_message:
    numbers = ''.join([digit for digit in word if digit.isdigit()])
    characters = [character for character in word if character.isalpha()]
    first_character = chr(int(numbers))
    characters[0], characters[-1] = characters[-1], characters[0]
    second_characters = ''.join(characters)
    final_message += first_character + second_characters + ' '

print(final_message)
    
