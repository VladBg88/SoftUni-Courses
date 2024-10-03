def calculator(command, a, b):
    if command == "multiply":
        return a * b
    elif command == "divide":
        return a / b
    elif command == "add":
        return a + b
    elif command == "subtract":
        return a - b
    else:
        return "Invalid operator"


command = input()
a = int(input())
b = int(input())

print(int(calculator(command, a, b)))
