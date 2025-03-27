def extract_parentheses(expression):
    stack = []

    for i, char in enumerate(expression):
        if char == "(":
            stack.append(i)  # Store index of '('
        elif char == ")":
            start_index = stack.pop()  # Get last unmatched '(' index
            print(expression[start_index : i + 1])  # Extract and print substring

# Example usage
expression = input()
extract_parentheses(expression)
