GOAL = 10000
count_steps = 0

while True:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        count_steps += steps
        if count_steps >= GOAL:
            print(f"Goal reached! Good job!")
            print(f"{count_steps - GOAL} steps over the goal!")
        elif count_steps < GOAL:
            print(f"{GOAL - count_steps} more steps to reach goal.")
        break

    count_steps += int(steps)

    if count_steps >= GOAL:
        print(f"Goal reached! Good job!")
        print(f"{count_steps - GOAL} steps over the goal!")
        break
