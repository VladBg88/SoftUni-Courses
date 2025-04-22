numbers_data = list(map(int, input().split()))


def swap(index1: int, index2: int):
    global numbers_data
    numbers_data[index1], numbers_data[index2] = numbers_data[index2], numbers_data[index1]
    return numbers_data


def multiply(index1: int, index2: int):
    global numbers_data
    numbers_data[index1] *= numbers_data[index2]
    return numbers_data


def decrease():
    global numbers_data
    numbers_data = [element - 1 for element in numbers_data]


def main_program():
    while True:
        user_data = input().split()
        if len(user_data) == 3:
            command, user_index1, user_index2 = user_data
        elif len(user_data) == 1:
            command = user_data[0]

        if command == 'end':
            break
        if command == 'swap'.strip():
            swap(int(user_index1), int(user_index2))

        elif command == 'multiply':
            multiply(int(user_index1), int(user_index2))

        elif command == 'decrease':
            decrease()

    print(', '.join(map(str, numbers_data)))


main_program()
