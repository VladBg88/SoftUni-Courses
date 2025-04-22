def palindrome_checking(palindrome_candidates: list):
    checking_list = []
    for element in palindrome_candidates:
        checking_list.append(element[::-1])

    for step in range(len(palindrome_candidates)):
        if palindrome_candidates[step] == checking_list[step]:
            print("True")
        else:
            print("False")


user_palindrome_candidates = input().split(", ")
palindrome_checking(user_palindrome_candidates)
