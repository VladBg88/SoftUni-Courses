def no_vowels(text: str):
    new_text = [x for x in text if x not in ('a', 'A', 'o', 'O', 'u', 'U', 'e', 'E', 'i', 'I')]
    print(''.join(new_text))


user_input = input().strip()
no_vowels(user_input)
