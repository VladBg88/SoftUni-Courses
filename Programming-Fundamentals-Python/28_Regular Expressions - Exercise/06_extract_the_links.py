import re

text = input()
pattern = r"([w]{3}.([A-Za-z0-9\-]+)(\.+[a-z\.]+)+)\b"

while text:
    matches = re.search(pattern, text)
    if matches:
        print(matches.group(1))

    text = input()