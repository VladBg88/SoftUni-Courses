hours_input = int(input())
minutes_input = int(input())

minutes = minutes_input + 15

if minutes >= 60:
    minutes -= 60
    hours_input += 1

if hours_input > 23:
    hours_input = 0


if minutes < 10:
    print(f'{hours_input}:0{minutes}')
else:
    print(f'{hours_input}:{minutes}')