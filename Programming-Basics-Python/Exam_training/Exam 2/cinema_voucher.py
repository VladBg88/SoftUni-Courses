voucher_value = int(input())
ticket_counter = 0
other_purchases_counter = 0

while True:
    command = input()
    if command == "End":
        break

    if len(command) > 8:
        value = ord(command[0]) + ord(command[1])
        if value <= voucher_value:
            ticket_counter += 1
    elif len(command) <= 8:
        value = ord(command[0])
        if value <= voucher_value:
            other_purchases_counter += 1

    if value > voucher_value:
        break

    voucher_value -= value

print(ticket_counter)
print(other_purchases_counter)
