user_input = input()
stack = []
reversed_string = ""

for char in user_input:
    stack.append(char)

while stack:
    reversed_string += stack.pop()

print(reversed_string)
