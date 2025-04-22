hall_capacity = int(input())
left_places = hall_capacity
income = 0

while True:
    people_incoming = input()
    if people_incoming == "Movie time!":
        print(f'There are {left_places} seats left in the cinema.')
        break

    if left_places < int(people_incoming):
        print(f'The cinema is full.')
        break

    left_places -= int(people_incoming)

    if int(people_incoming) % 3 == 0:
        income += int(people_incoming) * 5 - 5
    else:
        income += int(people_incoming) * 5

print(f'Cinema income - {income} lv.')
