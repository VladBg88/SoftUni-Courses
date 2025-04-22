from collections import deque

user_input = deque(input())
opening_brackets = "[{("
closing_brackets = "]})"
turns_counter = 0

while user_input and turns_counter < len(user_input) // 2:
    if user_input[0] in closing_brackets:
        break
    index = opening_brackets.index(user_input[0])
    if user_input[1] == closing_brackets[index]:
        user_input.popleft()
        user_input.popleft()
        user_input.rotate(turns_counter)
        turns_counter = 0
    else:
        user_input.rotate(-1)
        turns_counter += 1

if user_input:
    print("NO")
else:
    print("YES")
