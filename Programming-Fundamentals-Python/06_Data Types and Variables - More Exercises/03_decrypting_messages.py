key = int(input())
number_of_lines = int(input())
decrypt = ''

for i in range(number_of_lines):
    char = input()
    secret_char = ord(char) + key
    decrypt += chr(secret_char)

print(decrypt)
