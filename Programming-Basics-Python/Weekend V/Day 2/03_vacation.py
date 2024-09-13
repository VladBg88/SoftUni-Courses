needed_money_for_vacation = float(input())
current_money = float(input())
days_counter = 0
spending_days_counter = 0

while True:
    command = str(input())
    days_counter += 1

    if command == "spend":
        spend = float(input())
        current_money -= spend
        if current_money <= 0:
            current_money = 0

        spending_days_counter += 1

        if spending_days_counter >= 5:
            print("You can't save the money.")
            print(days_counter)
            break

    if command == "save":
        save = float(input())
        current_money += save
        if current_money >= needed_money_for_vacation:
            print(f"You saved the money for {days_counter} days.")
            break

    if command == "save":
        spending_days_counter = 0
