STARTING_HEIGHT = 5364
TOP_PEAK = 8848
days_counter = 1

while True:
    if days_counter == 5:
        break
    action = str(input())
    if action == 'END':
        break

    if action == 'Yes':
        days_counter += 1

    getting_up = int(input())
    STARTING_HEIGHT += getting_up

    if STARTING_HEIGHT >= TOP_PEAK:
        print(f"Goal reached for {days_counter} days!")
        break

if STARTING_HEIGHT < TOP_PEAK:
    print("Failed!")
    print(f"{STARTING_HEIGHT}")
elif STARTING_HEIGHT >= TOP_PEAK:
    print(f"Goal reached for {days_counter} days!")
