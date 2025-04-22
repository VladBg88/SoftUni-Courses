raw_input = input()

while True:
    user_input = input()
    if user_input == "Generate":
        print(f"Your activation key is: {raw_input}")
        break
    elif user_input.startswith('Contains'):
        substring = user_input.split('>>>')[1]
        print(f"{raw_input} contains {substring}" if substring in raw_input else f"Substring not found!")
    elif user_input.startswith('Flip'):
        second_command = user_input.split('>>>')[1]
        start_index = int(user_input.split('>>>')[2])
        end_index = int(user_input.split('>>>')[3])
        if second_command == 'Upper':
            raw_input = raw_input[:start_index] + raw_input[start_index:end_index].upper() + raw_input[end_index:]
        elif second_command == 'Lower':
            raw_input = raw_input[:start_index] + raw_input[start_index:end_index].lower() + raw_input[end_index:]
        print(raw_input)

    elif user_input.startswith('Slice'):
        start_index = int(user_input.split('>>>')[1])
        end_index = int(user_input.split('>>>')[2])
        raw_input = raw_input[:start_index] + raw_input[end_index:]
        print(raw_input)



