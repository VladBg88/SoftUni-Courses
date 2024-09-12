n = int(input())

for i in range(n):
    check_string = input()

    if ',' in check_string or '.' in check_string or '_' in check_string:
        print(f'{check_string} is not pure!')
    else:
        print(f'{check_string} is pure.')
