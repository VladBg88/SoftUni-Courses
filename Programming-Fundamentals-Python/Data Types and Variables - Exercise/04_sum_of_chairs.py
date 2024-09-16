lines_number = int(input())
total_sum = 0

for lines in range(lines_number):
    command = input()
    total_sum += ord(command)

print(f'The sum equals: {total_sum}')
