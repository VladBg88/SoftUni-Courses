def sorting_names(list_of_names: []):
    list_of_names = list_of_names.split(", ")
    sorted_list = sorted(list_of_names, key=lambda x: (-len(x), x))

    print(sorted_list)


user_list = input()
sorting_names(user_list)
