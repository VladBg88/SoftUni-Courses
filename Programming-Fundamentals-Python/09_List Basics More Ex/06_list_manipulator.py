import sys

initial_list = list(map(int, input().split()))

while True:
    command = input().split()
    if command[0] == "end":
        break

    action = command[0]

    if action == 'exchange':
        index = int(command[1])
        if 0 > index or index >= len(initial_list):
            print('Invalid index')
            continue
        initial_list = initial_list[index + 1:] + initial_list[:index + 1]

    elif action == 'max':
        even_odd = command[1]
        max_index = -1
        max_number = -sys.maxsize
        for idx, number in enumerate(initial_list):
            if (even_odd == 'even' and number % 2 == 0) or (even_odd == 'odd' and number % 2 != 0):
                if number >= max_number:
                    max_index = idx
                    max_number = number
        print("No matches" if max_index == -1 else max_index)

    elif action == 'min':
        even_odd = command[1]
        min_index = -1
        min_number = sys.maxsize
        for idx, number in enumerate(initial_list):
            if (even_odd == 'even' and number % 2 == 0) or (even_odd == 'odd' and number % 2 != 0):
                if number <= min_number:
                    min_index = idx
                    min_number = number
        print("No matches" if min_index == -1 else min_index)

    elif action == 'first':
        count = int(command[1])
        even_odd = command[2]
        first_even_list = []
        first_odd_list = []
        if count > len(initial_list):
            print("Invalid count")
            continue
        result = [num for num in initial_list if (num % 2 == 0 and even_odd == 'even') or
                  (num % 2 != 0 and even_odd == 'odd')][:count]
        print(result)

    elif action == 'last':
        count = int(command[1])
        even_odd = command[2]
        if count > len(initial_list):
            print("Invalid count")
            continue
        result = [num for num in initial_list if (num % 2 == 0 and even_odd == 'even') or
                  (num % 2 != 0 and even_odd == 'odd')][-count:]
        print(result)


print(initial_list)
