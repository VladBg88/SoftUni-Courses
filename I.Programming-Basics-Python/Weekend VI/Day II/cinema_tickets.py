FINAL_STOP_STRING = 'Finish'
MOVIE_STOP_STRING = 'End'

TICKET_TYPE_STANDARD = 'standard'
TICKET_TYPE_STUDENT = 'student'
TICKET_TYPE_KID = 'kid'

all_tickets = 0
sum_standard_tickets = 0
sum_student_tickets = 0
sum_kids_tickets = 0

while True:
    movie_name = input()
    if movie_name == FINAL_STOP_STRING:
        break
    seats_in_cinema = int(input())
    seats_taken = 0
    while seats_taken < seats_in_cinema:
        ticket_type = input()
        if ticket_type == MOVIE_STOP_STRING:
            break

        all_tickets += 1
        seats_taken += 1
        if ticket_type == TICKET_TYPE_STANDARD:
            sum_standard_tickets += 1
        elif ticket_type == TICKET_TYPE_STUDENT:
            sum_student_tickets += 1
        elif ticket_type == TICKET_TYPE_KID:
            sum_kids_tickets += 1

    print(f"{movie_name} - {seats_taken / seats_in_cinema * 100:.2f}% full.")

print(f"Total tickets: {all_tickets}")
print(f"{sum_student_tickets / all_tickets * 100:.2f}% student tickets.")
print(f"{sum_standard_tickets / all_tickets * 100:.2f}% standard tickets.")
print(f"{sum_kids_tickets / all_tickets * 100:.2f}% kids tickets.")
