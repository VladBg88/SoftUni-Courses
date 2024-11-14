import re

result = []
pattern = r"\d+"

while True:
    text = input()
    if text == "":
        break

    matches = re.findall(pattern, text)

    if matches:
        result.extend(matches)

print(" ".join(result))
