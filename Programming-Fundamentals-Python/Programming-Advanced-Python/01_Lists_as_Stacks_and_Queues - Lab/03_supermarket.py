from collections import deque

customers = deque()

user_input = input()

while user_input != "End":
    if user_input == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(user_input)

    user_input = input()

print(f"{len(customers)} people remaining.")
