all_groups = list(map(int, input().split(', ')))
boundary = 10
current_decade = [x for x in all_groups]

while current_decade:
    current_decade = [num for num in current_decade if num <= boundary]
    print(f"Group of {boundary}'s: {current_decade}")
    current_decade = [num for num in all_groups if num > boundary]
    boundary += 10
