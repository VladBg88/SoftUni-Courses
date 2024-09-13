command = int(input())

for i in range(command):
    if i == 0 or i == command - 1:
        print('*' * command)
    else:
        print('*' + (' ' * (command - 2) + '*'))
