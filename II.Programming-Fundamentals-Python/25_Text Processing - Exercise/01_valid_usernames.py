import re

all_usernames = input().split(", ")
pattern = r"^[A-Za-z0-9_-]{3,16}$"

for username in all_usernames:
    if re.match(pattern, username):
        print(username)
