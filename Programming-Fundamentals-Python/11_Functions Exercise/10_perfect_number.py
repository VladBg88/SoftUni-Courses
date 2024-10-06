def perfect_number(number):
    shadow_number = 0
    for i in range(1, number):
        if number % i == 0:
            shadow_number += i

    if shadow_number == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


user_input = int(input())
perfect_number(user_input)
