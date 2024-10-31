user_characters = input().split(', ')
ascii_dict = {char: ord(char) for char in user_characters}
print(ascii_dict)
