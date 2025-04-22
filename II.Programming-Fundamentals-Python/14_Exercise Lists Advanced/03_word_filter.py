user_list = input().split()
even_len_list = [word for word in user_list if len(word) % 2 == 0]
for word in even_len_list:
    print(word)
