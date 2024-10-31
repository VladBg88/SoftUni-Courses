numbers = input().split()
average = round((sum(map(int, numbers)) / len(numbers)), 2)
numbers = [int(element) for element in numbers if int(element) > average]
numbers = sorted(numbers, reverse=True)

if not numbers:
    print('No')
else:
    print(*numbers[:5])
