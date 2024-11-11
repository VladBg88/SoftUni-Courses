line = input().split()
line = [word * len(word) for word in line]
print("".join(line))