number = int(input())
number_counter = 1
col_counter = 1
while number_counter <= number:
    for _ in range(col_counter):
        print(number_counter, end=" ")
        number_counter += 1
        if number_counter > number:
            break
    print()
    col_counter += 1