line = input()
final_string = ""
working_string = ""

for char in range(len(line)):
    if line[char].isdigit():
        number = line[char]
        if len(line) > char + 1 and line[char + 1].isdigit():
            number = line[char] + line[char + 1]
        working_string *= int(number)
        final_string += working_string
        working_string = ""
    else:
        working_string += line[char].upper()

unique_symbols = len(set(final_string))

print(f"Unique symbols used: {unique_symbols}")
print(final_string)
