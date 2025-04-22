left_boundary = input()
right_boundary = input()
string = input()
found_characters = []
sum_ascii = []

for char in string:
    if ord(char) in range(ord(left_boundary) + 1, ord(right_boundary)):
        found_characters += char
        sum_ascii.append(ord(char))

print(sum(sum_ascii))
