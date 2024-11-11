line = input()

for i in range(len(line)):
    if line[i] == ":":
        print(f":{line[i + 1]}")
