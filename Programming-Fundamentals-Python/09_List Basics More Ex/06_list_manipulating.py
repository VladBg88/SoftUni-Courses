numbers = list(map(int, input().split()))


command = input()

while command != 'end':
    manipulating_command = command.split()

# "exchange {index}" – splits the list after the given index
# and exchanges the places of the two resulting sub-lists
    if manipulating_command[0] == 'exchange':
        after_split = []
        splitting_index = int(manipulating_command[1])
        if splitting_index < 0 or splitting_index > len(numbers):
            print('Invalid index')
            # break
        left_part = numbers[:(splitting_index + 1)]
        right_part = numbers[(splitting_index + 1):]

        for i in range(len(right_part)):
            after_split.append(right_part[i])
        for j in range(len(left_part)):
            after_split.append(left_part[j])
        numbers = after_split

# "max even/odd"– returns the INDEX of the max even/odd element.
    if manipulating_command[0] == 'max':
        max_odd = min(numbers)
        max_odd_counter = 0
        max_even = min(numbers)
        max_even_counter = 0
        if manipulating_command[1] == 'even':
            for index in range(len(numbers) - 1, -1, -1):
                if numbers[index] % 2 != 0:
                    continue
                else:
                    if numbers[index] >= max_even:
                        max_even = numbers[index]
                        max_even_counter += 1
            if max_even_counter > 1:
                for index in range(len(numbers) - 1, -1, -1):
                    if numbers[index] == max_even:
                        max_even = numbers[index]
                        # print(numbers.index(max_even))
                        break
            if max_even == min(numbers):
                print('No matches')
            else:
                print(numbers.index(max_even))

        elif manipulating_command[1] == 'odd':
            for index in range(len(numbers) - 1, -1, -1):
                if numbers[index] % 2 == 0:
                    continue
                else:
                    if numbers[index] >= max_odd:
                        max_odd = numbers[index]
                        max_odd_counter += 1
            if max_odd_counter > 1:
                for index in range(len(numbers) - 1, -1, -1):
                    if numbers[index] == max_odd:
                        max_odd = numbers[index]
                        #print(numbers.index(max_odd))
                        break
            if max_odd == min(numbers):
                print('No matches')
            else:
                print(numbers.index(max_odd))



# "min even/odd" – returns the INDEX of the min even/odd element
    elif manipulating_command[0] == 'min':
        min_odd = max(numbers)
        min_odd_counter = 0
        min_even = max(numbers)
        min_even_counter = 0
        if manipulating_command[1] == 'even':
            for index in range(len(numbers) - 1, -1, -1):
                if numbers[index] % 2 != 0:
                    continue
                else:
                    if numbers[index] <= min_even:
                        min_even = numbers[index]
                        min_even_counter += 1
            if min_even_counter > 1:
                for index in range(len(numbers) - 1, -1, -1):
                    if numbers[index] == min_even:
                        min_even = numbers[index]
                        # print(numbers.index(min_even))
                        break
            if min_even == max(numbers):
                print('No matches')
            else:
                print(numbers.index(min_even))
        elif  manipulating_command[1] == 'odd':
            for index in range(len(numbers) - 1, -1, -1):
                if numbers[index] % 2 == 0:
                    continue
                else:
                    if numbers[index] <= min_odd:
                        min_odd = numbers[index]
                        min_odd_counter += 1
            if min_odd_counter > 1:
                for index in range(len(numbers) - 1, -1, -1):
                    if numbers[index] == min_odd:
                        min_odd = numbers[index]
                        # print(numbers.index(min_odd))
                        break
            if min_odd == max(numbers):
                print('No matches')
            else:
                print(numbers.index(min_odd))


# "first {count} even/odd" – returns the first count even/odd elements
    if manipulating_command[0] == 'first' and int(manipulating_command[1]) <= len(numbers):
        counter = 0
        first_count_list = []
        for index in range(len(numbers)):
            if manipulating_command[2] == 'even':
                if numbers[index] % 2 == 0:
                    counter += 1
                    first_count_list.append(numbers[index])
                    if counter == int(manipulating_command[1]):
                    #     print(numbers[index])
                        break
                    else:
                        continue
            elif manipulating_command[2] == 'odd':
                if numbers[index] % 2 != 0:
                    counter += 1
                    first_count_list.append(numbers[index])
                    if counter == int(manipulating_command[1]):
                        #print(numbers[index])
                        break
                    else:
                        continue
        print(first_count_list)
    elif manipulating_command[0] == 'first' and int(manipulating_command[1]) > len(numbers):
        print('Invalid count')

# "last {count} even/odd" – returns the last count even/odd elements
    if manipulating_command[0] == 'last' and int(manipulating_command[1]) <= len(numbers):
        counter = 0
        last_count_list = []
        for index in range(len(numbers) -1, -1, -1):
            if manipulating_command[2] == 'even':
                if numbers[index] % 2 == 0:
                    counter += 1
                    last_count_list.append(numbers[index])
            elif manipulating_command[2] == 'odd':
                if numbers[index] % 2 != 0:
                    counter += 1
                    last_count_list.append(numbers[index])
        print(last_count_list)
    elif manipulating_command[0] == 'last' and int(manipulating_command[1]) > len(numbers):
        print('Invalid count')

    command = input()

print(numbers)






