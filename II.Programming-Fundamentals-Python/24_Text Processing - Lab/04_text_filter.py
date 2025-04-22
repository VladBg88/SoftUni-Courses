banned_words = input().split(", ")
line = input()

for word in banned_words:
    while word in line:
        line = line.replace(word, "*" * len(word))

print(line)
