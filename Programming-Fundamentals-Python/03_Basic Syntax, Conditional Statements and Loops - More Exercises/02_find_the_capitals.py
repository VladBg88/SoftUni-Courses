word = input()
capital_letters = []

for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90:
        capital_letters.append(i)

print(capital_letters)
