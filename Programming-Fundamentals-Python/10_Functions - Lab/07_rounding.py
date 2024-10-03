def round_elements(user_input):
    first_list = [float(element) for element in user_input]
    final_list = [round(element) for element in first_list]

    return final_list


user_list = input().split()
print(round_elements(user_list))
