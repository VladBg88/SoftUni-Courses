secret_word = ''
c_counter = 0
o_counter = 0
n_counter = 0

while True:
    symbol_input = str(input())
    if symbol_input == 'End':
        break

    if not symbol_input.isalpha():
        continue

    if symbol_input == 'c' and c_counter == 0:
        c_counter += 1
        if c_counter + o_counter + n_counter == 3:
            print(f'{secret_word}', end=' ')
            c_counter = 0
            o_counter = 0
            n_counter = 0
            secret_word = ''
        continue
    elif symbol_input == 'o' and o_counter == 0:
        o_counter += 1
        if c_counter + o_counter + n_counter == 3:
            print(f'{secret_word}', end=' ')
            c_counter = 0
            o_counter = 0
            n_counter = 0
            secret_word = ''
        continue
    elif symbol_input == 'n' and n_counter == 0:
        n_counter += 1
        if c_counter + o_counter + n_counter == 3:
            print(f'{secret_word}', end=' ')
            c_counter = 0
            o_counter = 0
            n_counter = 0
            secret_word = ''
        continue

    secret_word += symbol_input
