first_number = int(input())
total = 0
second_number = int(input())

while True:
    total += second_number
    if total >= first_number:
        print(total)
        break
    second_number = int(input())
