sequence_of_numbers = input().split()
characters = input()
message = ""
new_characters = ""

for num in sequence_of_numbers:
    total = 0
    for digit in num:
        total += int(digit)

    while total > len(characters):
        total -= len(characters)

    message += str(characters[total])

    for i in range(len(characters)):
        if i == total:
            continue
        else:
            new_characters += characters[i]

    characters = new_characters
    new_characters = ""

print(message)
