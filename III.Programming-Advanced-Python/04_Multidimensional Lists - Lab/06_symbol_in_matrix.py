matrix_size = int(input())
matrix = [[x for x in input()] for x in range(matrix_size)]
stop = False

find_symbol = input()

for row in range(matrix_size):
    if stop:
        break
    for col in range(matrix_size):
        if stop:
            break
        if find_symbol in matrix[row][col]:
            print(f"({row}, {col})")
            stop = True

if not stop:
    print(f"{find_symbol} does not occur in the matrix")