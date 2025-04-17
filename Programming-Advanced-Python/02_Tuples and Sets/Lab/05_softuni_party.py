vip_guests = set()
regular_guests = set()
command = ''

number_of_guests = int(input())

for line in range(number_of_guests):
    command = input()
    if len(command) == 8:
        if command[0].isdigit():
            vip_guests.add(command)
        else:
            regular_guests.add(command)

while command != 'END':
    command = input()
    if len(command) == 8:
        if command[0].isdigit() and command in vip_guests:
            vip_guests.remove(command)
        elif command in regular_guests:
            regular_guests.remove(command)

print(len(vip_guests) + len(regular_guests))
for code in sorted(vip_guests):
    print(code)
for code in sorted(regular_guests):
    print(code)

