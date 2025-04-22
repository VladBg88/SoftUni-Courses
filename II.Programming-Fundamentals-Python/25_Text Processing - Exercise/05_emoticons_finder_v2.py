line = input().split()

for word in line:
    if word.startswith(":") and len(word) > 1:
        print(f"{word[:2]}")