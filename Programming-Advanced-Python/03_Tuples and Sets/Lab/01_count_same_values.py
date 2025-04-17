user_input = [float(x) for x in input().split()]
database = {}

for num in user_input:
    if num not in database:
        database[num] = user_input.count(num)

for key, value in database.items():
    print(f"{key:.1f} - {value} times")