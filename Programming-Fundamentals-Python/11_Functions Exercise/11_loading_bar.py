def loading_bar(percentage):
    if percentage < 10:
        print(f"{percentage * 10}% [{percentage * '%'}{(10 - percentage) * '.'}]")
        print('Still loading...')
    elif percentage == 10:
        print('100% Complete!')
        print(f"[{10 * '%'}]")


user_input = int(input()) // 10
loading_bar(user_input)
