contest_data = {}
user_data = {}

while True:
    command = input().strip()
    if command == "no more time":
        break

    username, contest, points = command.split(" -> ")
    points = int(points)

    # Update contest data
    if contest not in contest_data:
        contest_data[contest] = {}

    if username in contest_data[contest]:
        if points > contest_data[contest][username]:
            user_data[username] += points - contest_data[contest][username]
            contest_data[contest][username] = points
    else:
        contest_data[contest][username] = points
        if username in user_data:
            user_data[username] += points
        else:
            user_data[username] = points

# Output contest standings
for contest, participants in contest_data.items():
    print(f"{contest}: {len(participants)} participants")
    sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
    for i, (username, points) in enumerate(sorted_participants, start=1):
        print(f"{i}. {username} <::> {points}")

# Output individual standings
print("Individual standings:")
sorted_users = sorted(user_data.items(), key=lambda x: (-x[1], x[0]))
for i, (username, total_points) in enumerate(sorted_users, start=1):
    print(f"{i}. {username} -> {total_points}")
