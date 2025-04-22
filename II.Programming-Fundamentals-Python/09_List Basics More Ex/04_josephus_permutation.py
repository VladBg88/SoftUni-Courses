all_people = input().split()
unlucky_number = int(input())
alive_people = all_people[:]
how_they_died = []

index = unlucky_number - 1

while len(alive_people) > 0:
    index = index % len(alive_people)
    how_they_died.append(int(alive_people.pop(index)))
    index += unlucky_number - 1

print(f"[{','.join(map(str, how_they_died))}]")
