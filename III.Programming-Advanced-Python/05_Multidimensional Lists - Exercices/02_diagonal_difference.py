matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
size = len(matrix)

primary_diagonal = sum([matrix[row][col] for row in range(size) for col in range(size) if row == col])
secondary_diagonal = sum([matrix[i][size - 1 - i] for i in range(size)])
difference = abs(primary_diagonal - secondary_diagonal)

print(difference)