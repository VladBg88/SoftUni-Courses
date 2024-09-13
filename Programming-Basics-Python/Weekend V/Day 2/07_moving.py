room_width = int(input())
room_length = int(input())
room_height = int(input())
user_command = ""
room_space = room_width * room_length * room_height
boxes_space = 0

while True:
    user_command = input()

    if user_command == "Done":
        print(f"{room_space - boxes_space} Cubic meters left.")
        break

    boxes_space += int(user_command)

    if boxes_space >= room_space:
        print(f"No more free space! You need {boxes_space - room_space} Cubic meters more.")
        break
