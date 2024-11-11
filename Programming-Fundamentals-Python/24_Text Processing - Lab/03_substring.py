key_string = input()
line = input()

while True:
    if key_string not in line:
        break
    else:
        line = line.replace(key_string, "")

print(line)
