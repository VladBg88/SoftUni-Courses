line = input()
new_string = ''
check_repeat = ''

for i in range(len(line)):
    if line[i] != check_repeat:
        new_string += line[i]
        check_repeat = line[i]

print(new_string)