number_of_lines = int(input())
even = []
odd = []
negative = []
positive = []

for i in range(number_of_lines):
    numbers = int(input())

    if numbers == 0:
        positive.append(numbers)
        even.append(numbers)
    elif numbers < 0:
        negative.append(numbers)
        if numbers % 2 == 0:
            even.append(numbers)
        else:
            odd.append(numbers)
    elif numbers > 0:
        positive.append(numbers)
        if numbers % 2 == 0:
            even.append(numbers)
        else:
            odd.append(numbers)

command = input().lower()
if command == 'even':
    print(even)
elif command == 'odd':
    print(odd)
elif command == 'negative':
    print(negative)
elif command == 'positive':
    print(positive)
