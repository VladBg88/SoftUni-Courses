matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
size = len(matrix)

primary_diagonal = [matrix[row][col] for row in range(size) for col in range(size) if row == col]
secondary_diagonal = [matrix[i][size - 1 - i] for i in range(size)]


print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum(secondary_diagonal)}")
