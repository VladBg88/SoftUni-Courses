import math

word = 'Go Fuck Yourself!'
best_word = ""
best_score = 0

while True:
    word = str(input())
    if word == 'End of words':
        break
    word_length = len(word)
    total_sum = 0

    for symbol in range(word_length):
        total_sum += ord(word[symbol])

    if word[0] not in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
        total = math.floor(total_sum / word_length)
    else:
        total = total_sum * word_length

    if total >= best_score:
        best_score = total
        best_word = word

    total_sum = 0
    total = 0

print(f'The most powerful word is {best_word} - {best_score}')
