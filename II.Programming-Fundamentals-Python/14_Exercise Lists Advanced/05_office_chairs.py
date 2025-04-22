number_of_rooms = int(input())
total_free_chairs = 0
check = True

for i in range(number_of_rooms):
    information = input().split()
    if len(information[0]) < int(information[1]):
        print(f"{int(information[1]) - len(information[0])} more chairs needed in room {i + 1}")
        check = False
    else:
        total_free_chairs += (len(information[0]) - int(information[1]))

if check:
    print(f"Game On, {total_free_chairs} free chairs left")
