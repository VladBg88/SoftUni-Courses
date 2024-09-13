name_of_player_one = str(input())
name_of_player_two = str(input())
count_a = 0
count_b = 0
a = ""
b = ""

while True:
    a = input()
    if a == "End of game":
        break
    b = input()

    if int(a) > int(b):
        count_a += int(a) - int(b)
    elif int(a) < int(b):
        count_b += int(b) - int(a)

    if int(a) == int(b):
        a = input()
        b = input()
        print("Number wars!")
        if int(a) > int(b):
            # count_a += int(a) - int(b)
            print(f"{name_of_player_one} is winner with {count_a} points")
        elif int(a) < int(b):
            # count_b += int(b)
            print(f"{name_of_player_two} is winner with {count_b} points")
        exit()

print(f"{name_of_player_one} has {count_a} points")
print(f"{name_of_player_two} has {count_b} points")
