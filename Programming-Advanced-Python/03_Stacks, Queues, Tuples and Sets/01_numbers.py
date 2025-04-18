user_set_one = set(map(int, input().split()))
user_set_two = set(map(int, input().split()))
number = int(input())

for _ in range(number):
    user_input = input().split()
    new_numbers = []
    command = user_input[0] + user_input[1]
    new_numbers = set(map(int, user_input[2:]))

    if command == "AddFirst":
        user_set_one.update(new_numbers)
    elif command == "AddSecond":
        user_set_two.update(new_numbers)
    elif command == "RemoveFirst":
        user_set_one.difference_update(new_numbers)
    elif command == "RemoveSecond":
        user_set_two.difference_update(new_numbers)
    elif command == "CheckSubset":
        print(user_set_one <= user_set_two or user_set_two <= user_set_one)

print(*sorted(user_set_one), sep=', ')
print(*sorted(user_set_two), sep=', ')
