numbers = input().split()

# Calculate average
average = sum(map(int, numbers)) / len(numbers)

# Filter numbers greater than the average
numbers = [int(element) for element in numbers if int(element) > average]

# Sort the filtered numbers based on the average condition
if average < 0:
    numbers = sorted(numbers)  # Ascending order if average < 0
else:
    numbers = sorted(numbers, reverse=True)  # Descending order if average >= 0

# Get the first 5 numbers if there are any
result = numbers[:5]

# Check if there are any numbers to display
if not result:  # This checks if the list is empty after filtering
    print('No')
else:
    print(*result)  # Print the numbers space-separated
