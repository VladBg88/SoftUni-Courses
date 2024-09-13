while True:
    word = input()
    if word == 'End':
        exit()
    elif word == 'SoftUni':
        continue

    for i in range(len(word)):
        print(word[i] * 2, end='')

    print()
