sequence_of_numbers = input().split()
characters = input()
message = ""

for num in sequence_of_numbers:
    total = 0
    for digit in num:
        total += int(digit)

    total = total % len(characters)
    message += characters[total]
    characters = characters[:total] + characters[total+1:]

print(message)
