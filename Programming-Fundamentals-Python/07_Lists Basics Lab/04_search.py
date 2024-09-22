number_of_lines = int(input())
special_word = input()
string_container = []

for i in range(number_of_lines):
    word = input()
    string_container.append(word)

print(string_container)

for i in range(len(string_container) - 1, -1, -1):
    element = string_container[i]
    if special_word not in element:
        string_container.remove(element)

print(string_container)
