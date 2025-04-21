MAIN_COLORS = ["red", "yellow", "blue"]
SECONDARY_COLORS = ["orange", "purple", "green"]

user_input = input().split()
colors = []

while user_input:
    second_new_word = ''
    if len(user_input) > 1:
        first_old_word = user_input.pop(0)
        second_old_word = user_input.pop(-1)
        first_new_word = first_old_word + second_old_word
        second_new_word = second_old_word + first_old_word
    else:
        first_old_word = user_input.pop()
        first_new_word = first_old_word

    if first_new_word in MAIN_COLORS or first_new_word in SECONDARY_COLORS:
        colors.append(first_new_word)
    elif second_new_word in MAIN_COLORS or second_new_word in SECONDARY_COLORS:
        colors.append(second_new_word)
    else:
        # Reinsert shortened versions if length > 1
        words_to_shorten = [first_old_word]
        if 'second_old_word' in locals():
            words_to_shorten.append(second_old_word)

        for word in words_to_shorten:
            if len(word) > 1:
                user_input.insert(len(user_input) // 2, word[:-1])

# Validate secondary colors based on required primaries
required_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

for secondary, required in required_colors.items():
    if secondary in colors and not required.issubset(colors):
        colors.remove(secondary)

print(colors)
