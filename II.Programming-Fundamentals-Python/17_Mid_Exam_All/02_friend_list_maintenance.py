def main_program():
    friend_list = input().split(', ')
    while True:
        command = input().split()
        if command[0] == 'Report':
            break

        if command[0] == 'Blacklist':
            name_blacklisted = command[1]
            if name_blacklisted in friend_list:
                print(f"{name_blacklisted} was blacklisted.")
                friend_list = ['Blacklisted' if name == name_blacklisted else name for name in friend_list]
            else:
                print(f'{name_blacklisted} was not found.')
        elif command[0] == 'Error':
            index = int(command[1])
            if 0 <= index <= len(friend_list) - 1 and friend_list[index] != 'Blacklisted' and friend_list[index] != 'Lost':
                print(f"{friend_list[index]} was lost due to an error.")
                friend_list[index] = 'Lost'
        elif command[0] == 'Change':
            index = int(command[1])
            new_name = command[2]
            if 0 <= index <= len(friend_list) - 1:
                print(f"{friend_list[index]} changed his username to {new_name}.")
                friend_list[index] = new_name

    blacklisted_count = 0
    lost_names_count = 0
    for element in friend_list:
        if element == 'Blacklisted':
            blacklisted_count += 1
        elif element == 'Lost':
            lost_names_count += 1

    print(f"Blacklisted names: {blacklisted_count}")
    print(f"Lost names: {lost_names_count}")
    print(*friend_list)


main_program()
