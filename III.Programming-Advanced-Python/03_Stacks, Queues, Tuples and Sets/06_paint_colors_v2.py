ALL_COLORS = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
COLOR_REQUIREMENTS = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

user_string = input().split()
crafted_colors = []

while user_string:
    first_word = user_string.pop(0)
    if user_string:
        second_word = user_string.pop(-1)

        for combo in (first_word + second_word, second_word + first_word):
                if combo in ALL_COLORS:
                    crafted_colors.append(combo)
                    break
        else:
            for word in (first_word, second_word):
                if len(word) > 1:
                    user_string.insert(len(user_string) // 2, word[:-1])
    else:
        if first_word in ALL_COLORS:
            crafted_colors.append(first_word)


for color, requirements in COLOR_REQUIREMENTS.items():
    if color in crafted_colors and not requirements.issubset(crafted_colors):
        crafted_colors.remove(color)

print(crafted_colors)