import re

numbers = list(map(int, input().split()))
result = ''

while True:
    command = input()
    if command == "find":
        break

    for i in range(len(command)):
        if i >= len(numbers):
            key = i % len(numbers)
            result += chr(ord(command[i]) - numbers[key])
            continue
        result += chr(ord(command[i]) - numbers[i])

    match_treasure = re.search(r'&(.+?)&', result)
    match_coordinates = re.search(r'<(.+?)>', result)

    if match_treasure and match_coordinates:
        treasure = match_treasure.group(1)
        coordinates = match_coordinates.group(1)

        print(f"Found {treasure} at {coordinates}")

    result = ''

