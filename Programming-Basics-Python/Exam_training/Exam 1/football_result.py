first_match = str(input())
second_match = str(input())
third_match = str(input())

win_counter = 0
drawn_counter = 0
loss_counter = 0

a = int(first_match[0])
b = int(first_match[2])
c = int(second_match[0])
d = int(second_match[2])
e = int(third_match[0])
f = int(third_match[2])

if a > b:
    win_counter += 1
elif a == b:
    drawn_counter += 1
elif a < b:
    loss_counter += 1

if c > d:
    win_counter += 1
elif c == d:
    drawn_counter += 1
elif c < d:
    loss_counter += 1

if e > f:
    win_counter += 1
elif e == f:
    drawn_counter += 1
elif e < f:
    loss_counter += 1

print(f"Team won {win_counter} games.")
print(f"Team lost {loss_counter} games.")
print(f"Drawn games: {drawn_counter}")
