number_of_line = int(input())
balance = 0
balanced = True

for i in range(number_of_line):
    command = input().strip()

    if len(command) != 1:
        continue

    if ord(command) == 40:
        balance += 1
        if balance > 1:
            break
    elif ord(command) == 41:
        balance -= 1
        if balance < 0:
            balanced = False
            break

if balance == 0 and balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
