student = 0
standard = 0
kid = 0

while True:
    movie_title = input()
    if movie_title == "Finish":
        break
    room_capacity = int(input())
    total_seets = room_capacity

    while True:
        if total_seets == 0:
            break

        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student += 1
        elif ticket_type == "standard":
            standard += 1
        elif ticket_type == "kid":
            kid += 1

        total_seets -= 1

    print(f"{movie_title} - {100 - (total_seets / room_capacity * 100):.2f}% full. ")

all_tickets = student + standard + kid
print(f"Total tickets: {all_tickets}")
print(f"{student / all_tickets * 100:.2f}% student tickets.")
print(f"{standard / all_tickets * 100:.2f}% standard tickets.")
print(f"{kid / all_tickets * 100:.2f}% kids tickets.")

