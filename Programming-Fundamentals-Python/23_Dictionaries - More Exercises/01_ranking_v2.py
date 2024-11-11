contest_dictionary = {}
approved_users = {}

while True:
    command = input()
    if command == "end of contests":
        break
    command = command.split(":")
    contest_name, contest_password = command[0], command[1]

    if contest_name not in contest_dictionary:
        contest_dictionary[contest_name] = []
    contest_dictionary[contest_name].append(contest_password)

while True:
    command = input()
    if command == "end of submissions":
        break
    command = command.split("=>")
    contest_name, contest_password, username, usr_points = command[0], command[1], command[2], int(command[3])

    if contest_name not in contest_dictionary or contest_password not in contest_dictionary[contest_name]:
        continue

    if username not in approved_users:
        approved_users[username] = {}

    if contest_name not in approved_users[username] or approved_users[username][contest_name] < usr_points:
        approved_users[username][contest_name] = usr_points

best_user = ""
best_points = 0

user_totals = {user: sum(scores.values()) for user, scores in approved_users.items()}

for user, total_points in user_totals.items():
    if total_points > best_points:
        best_user = user
        best_points = total_points

print(f"Best candidate is {best_user} with total {best_points} points.")
print("Ranking:")

for user, contests in sorted(approved_users.items()):
    print(f"{user}")
    for contest, points in sorted(contests.items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
