list_of_coffees = input().split()
number_of_commands = int(input())


def include(coffee, user_list_of_coffees):
    user_list_of_coffees.append(coffee)
    return user_list_of_coffees


def remove(first_or_last, number_of_coffees, user_list_of_coffees):
    if first_or_last == 'first' and len(user_list_of_coffees) > int(number_of_coffees):
        user_list_of_coffees = user_list_of_coffees[int(number_of_coffees):]
    elif first_or_last == 'last' and len(user_list_of_coffees) > int(number_of_coffees):
        user_list_of_coffees = user_list_of_coffees[:len(list_of_coffees) - int(number_of_coffees)]
    return user_list_of_coffees


def prefer(coffee_one, coffee_two, user_list_of_coffees):
    if 0 <= coffee_one <= len(user_list_of_coffees) - 1 and 0 <= coffee_two <= len(user_list_of_coffees) - 1:
        user_list_of_coffees[coffee_one], user_list_of_coffees[coffee_two] = user_list_of_coffees[coffee_two], user_list_of_coffees[coffee_one]
    return user_list_of_coffees


def reverse(user_list_of_coffees):
    user_list_of_coffees.reverse()
    return user_list_of_coffees


def main_program():
    global list_of_coffees
    for turn in range(number_of_commands):
        command = input().split()

        if 'Include' in command:
            list_of_coffees = include(command[1], list_of_coffees)
        elif 'Remove' in command:
            list_of_coffees = remove(command[1], command[2], list_of_coffees)
        elif 'Prefer' in command:
            list_of_coffees = prefer(int(command[1]), int(command[2]), list_of_coffees)
        elif 'Reverse' in command:
            list_of_coffees = reverse(list_of_coffees)

    print("Coffees:")
    print(*list_of_coffees)


main_program()
