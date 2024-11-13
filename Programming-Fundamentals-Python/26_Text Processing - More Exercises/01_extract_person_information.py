import re

turns = int(input())
for turn in range(turns):
    text = input()

    match_name = re.search(r'@(.+?)\|', text)
    match_age = re.search(r'#(.+?)\*', text)
    if match_name and match_age:
        print(f"{match_name.group(1)} is {match_age.group(1)} years old.")
