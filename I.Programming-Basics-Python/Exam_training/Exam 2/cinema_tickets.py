counter_student_ticket = 0
counter_standard_ticket = 0
counter_kid_ticket = 0


while True:
    name_of_movie = str(input())
    if name_of_movie == "Finish":
        break
    free_seats = int(input())
    total_seats = free_seats

    while True:
        if free_seats == 0:
            break

        ticket_type = str(input())

        if ticket_type == "End":
            break

        if ticket_type == "student":
            counter_student_ticket += 1
        elif ticket_type == "standard":
            counter_standard_ticket += 1
        elif ticket_type == "kid":
            counter_kid_ticket += 1

        free_seats -= 1

    print(f"{name_of_movie} - {100 - 100 / total_seats * free_seats:.2f}% full.")

all_tickets = counter_student_ticket + counter_standard_ticket + counter_kid_ticket
print(f"Total tickets: {all_tickets}")
print(f"{100 / all_tickets * counter_student_ticket:.2f}% student tickets.")
print(f"{100 / all_tickets * counter_standard_ticket:.2f}% standard tickets.")
print(f"{100 / all_tickets * counter_kid_ticket:.2f}% kids tickets.")
