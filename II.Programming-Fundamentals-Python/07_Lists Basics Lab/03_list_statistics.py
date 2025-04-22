number = int(input())
positive_numbers = []
negative_numbers = []

for i in range(number):
    command = int(input())
    if command >= 0:
        positive_numbers.append(command)
    else:
        negative_numbers.append(command)

print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {len(positive_numbers)}')
print(f'Sum of negatives: {sum(negative_numbers)}')
