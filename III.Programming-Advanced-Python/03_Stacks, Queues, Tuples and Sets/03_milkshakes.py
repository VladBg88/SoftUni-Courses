from collections import deque

milkshakes = 0
chocolates = deque(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))

while milkshakes < 5 and chocolates and milk_cups:

    while chocolates and chocolates[-1] <= 0:
        chocolates.pop()

    while milk_cups and milk_cups[0] <= 0:
        milk_cups.popleft()

    if not chocolates or not milk_cups:
        break

    chocolate = chocolates[-1]
    milk = milk_cups[0]

    if chocolate == milk:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5
        if chocolates[-1] <= 0:
            chocolates.pop()


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milk_cups)) if milk_cups else 'empty'}")
