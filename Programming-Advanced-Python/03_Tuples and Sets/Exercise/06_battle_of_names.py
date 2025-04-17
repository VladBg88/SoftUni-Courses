number_n = int(input())
odd_collection = set()
even_collection = set()

for row in range(1, number_n + 1):
    user_name = input()
    current_word = 0

    for symbol in user_name:
        current_word += ord(symbol)

    current_word = current_word // row
    if current_word % 2 == 0:
        even_collection.add(current_word)
    else:
        odd_collection.add(current_word)

if sum(odd_collection) == sum(even_collection):
    print(*odd_collection | even_collection, sep= ', ')
elif sum(odd_collection) > sum(even_collection):
    print(*odd_collection - even_collection, sep= ', ')
elif sum(even_collection) > sum(odd_collection):
    print(*odd_collection ^ even_collection, sep= ", ")