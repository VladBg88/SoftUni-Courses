dictionary_of_synonyms = {}
counter_words = int(input())

for i in range(counter_words):
    word = input()
    synonym = input()

    if word not in dictionary_of_synonyms:
        dictionary_of_synonyms[word] = []
    dictionary_of_synonyms[word].append(synonym)

for word, synonyms in dictionary_of_synonyms.items():
    print(f"{word} - {', '.join(synonyms)}")
