number = int(input())

string = str(number)

sorted_string = ''.join(sorted(string, reverse=True))

print(int(sorted_string))