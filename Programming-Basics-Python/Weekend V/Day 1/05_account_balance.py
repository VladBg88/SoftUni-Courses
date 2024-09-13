new_input = input()
total_sum = 0.0

while new_input != "NoMoreMoney":
    if float(new_input) < 0:
        print(f"Invalid operation!")
        break
    print(f"Increase: {float(new_input):.2f}")
    total_sum += float(new_input)
    new_input = input()

print(f"Total: {total_sum:.2f}")
