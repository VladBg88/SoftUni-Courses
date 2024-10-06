def data_types(user_type, user_data):
    if user_type == 'int':
        return int(user_data) * 2
    elif user_type == 'real':
        return f'{(float(user_data) * 1.5):.2f}'
    elif user_type == 'string':
        return f'${user_data}$'
    else:
        return 'Invalid input'


user_input_type = input()
user_input_data = input()
print(data_types(user_input_type, user_input_data))
