n = int(input())
usernames = set()

for _ in range(n):
    user_input = input()
    usernames.add(user_input)

for name in usernames:
    print(name)
