rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for row in range(rows)]
command = ''

while True:
    command = input().split()
    if command[0] == 'END':
        break

    if command[0] == 'swap' and len(command) == 5:
        try:
            row1, col1, row2, col2 = map(int, command[1:])
            if (
                0 <= row1 < rows and 0 <= col1 < cols and
                0 <= row2 < rows and 0 <= col2 < cols
            ):
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for row in matrix:
                    print(*row)
            else:
                print('Invalid input!')
        except ValueError:
            print('Invalid input!')
    else:
        print('Invalid input!')