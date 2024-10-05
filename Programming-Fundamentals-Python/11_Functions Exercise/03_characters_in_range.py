def characters_in_range(a, b):
    new_list = []
    for i in range(ord(a) + 1, ord(b)):
        new_list.append(chr(i))

    return new_list


input_a = input()
input_b = input()
print(*characters_in_range(input_a, input_b))
