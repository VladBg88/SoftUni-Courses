sequence_of_numbers = (input()).split()
int_sequence_of_numbers = [int(x) for x in sequence_of_numbers]


def even_numbers(x):
    return x % 2 == 0


list_of_even_numbers = list(filter(even_numbers, int_sequence_of_numbers))
print(list_of_even_numbers)
