def even_numbers():
    list_of_numbers = list(map(int, input().split(", ")))
    found_indices_or_no = map(
        lambda x: x if list_of_numbers[x] % 2 == 0 else 'no',
        range(len(list_of_numbers))
    )
    result = list(filter(lambda a: a != 'no', found_indices_or_no))
    print(result)


even_numbers()
