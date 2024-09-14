input_string = input().lower()

words_to_count = ["sand", "water", "fish", "sun"]

word_count = {word: input_string.count(word) for word in words_to_count}

total_count = sum(word_count.values())

print(total_count)
