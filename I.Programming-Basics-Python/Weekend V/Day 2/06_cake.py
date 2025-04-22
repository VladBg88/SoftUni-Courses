x = int(input())
y = int(input())

cake_total_pieces = x * y

while True:
    cake_pieces = input()

    if cake_pieces == "STOP":
        break

    cake_total_pieces -= int(cake_pieces)
    cake_pieces = 0

    if cake_total_pieces <= 0:
        break

if cake_total_pieces >= 0:
    print(f"{cake_total_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {int(cake_pieces) - cake_total_pieces} pieces more.")
