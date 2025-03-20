import re
counted_matches = []
counter = 0

text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(pattern, text)

for match in matches:
    counter += 1
    if match[1] == match[2][::-1]:
        counted_matches.append(match[1])

if counter:
    print(f"{counter} word pairs found!")
else:
    print("No word pairs found!")

if counted_matches:
    print(f"The mirror words are:")
    print(', '.join(f"{match} <=> {''.join(reversed(match))}" for match in counted_matches))
else:
    print("No mirror words!")
