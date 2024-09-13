last_sector = str(input())
rows_of_first_sector = int(input())
number_of_seats_of_odd = int(input())
counter_all_seats = 0

for i in range(65, ord(last_sector) + 1):
    if i > 65:
        rows_of_first_sector += 1
    for j in range(1, rows_of_first_sector + 1):
        if j % 2 == 0:
            seats = number_of_seats_of_odd + 2
        else:
            seats = number_of_seats_of_odd
        for k in range(1, seats + 1):
            print(f'{chr(i)}{j}{chr(k + 96)}')
            counter_all_seats += 1

print(counter_all_seats)