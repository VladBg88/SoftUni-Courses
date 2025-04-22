string1 = input()
string2 = input()

new_string = ''

for i in range(len(string1)):
    if string1[i] != string2[i]:
        new_string += string2[i]
        print(new_string + string1[i+1:])
    else:
        new_string += string1[i]
