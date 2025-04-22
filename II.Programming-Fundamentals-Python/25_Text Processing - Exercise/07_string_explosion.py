line = input()
final_string = ""
explosion_power = 0

for index in range(len(line)):
    if explosion_power > 0 and line[index] != ">":
        explosion_power -= 1

    elif line[index] == ">":
        final_string += line[index]
        explosion_power += int(line[index + 1])

    else:
        final_string += line[index]

print(final_string)