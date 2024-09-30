sequence_of_numbers = input().split()
characters = input()
message = ""

for num in sequence_of_numbers:
    total = 0
    for digit in num:
        total += int(digit)

    while total <= len(characters):
        total - len(characters)

    message += str(characters[total])

print(message)
