line = input().split()

for word in line:
    if word.startswith(":"):
        if not word.endswith((".", ",", "?", "!")):
            print(word)
        else:
            print(f"{word[:-1]}")