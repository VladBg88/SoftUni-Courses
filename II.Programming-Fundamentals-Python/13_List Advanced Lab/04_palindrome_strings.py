def palindrome_strings(sort_palindromes: [], special_palindrome: str):
    new_list = sort_palindromes.split()
    palindrome_list = []
    for word in new_list:
        if word == "".join(reversed(word)):
            palindrome_list.append(word)

    counter_special_palindrome = 0
    for word in palindrome_list:
        if word == special_palindrome:
            counter_special_palindrome += 1

    print(palindrome_list)
    print(f'Found palindrome {counter_special_palindrome} times')


user_list_palindromes = input()
user_special_palindrome = input()

palindrome_strings(user_list_palindromes, user_special_palindrome)
