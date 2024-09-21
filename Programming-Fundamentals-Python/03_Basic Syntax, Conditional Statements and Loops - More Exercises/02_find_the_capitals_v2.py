word = input()
capital_letter_indices = []

for i in range(len(word)):
    if word[i] == word[i].upper() and word[i] != ' ':
        capital_letter_indices.append(i)
print(capital_letter_indices)