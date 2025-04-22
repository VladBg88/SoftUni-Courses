def tribonacci_sequence(n):
    # Handle base cases
    if n == 1:
        print(1)
        return
    elif n == 2:
        print(1, 1)
        return
    elif n == 3:
        print(1, 1, 2)
        return

    # Start the sequence with the first three numbers
    tribonacci = [1, 1, 2]

    # Generate the rest of the sequence until we have n numbers
    for i in range(3, n):
        next_value = tribonacci[-1] + tribonacci[-2] + tribonacci[-3]
        tribonacci.append(next_value)

    # Print the sequence on one line separated by spaces
    print(" ".join(map(str, tribonacci)))


# Example usage
n = int(input())  # Input the number of terms you want to print
tribonacci_sequence(n)
