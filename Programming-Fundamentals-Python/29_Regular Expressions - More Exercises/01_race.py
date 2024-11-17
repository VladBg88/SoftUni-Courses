import re

participants = input().split(', ')
results = {}

while True:
    line = input()
    if line == 'end of race':
        break

    racer_name = re.sub(r"[^A-Za-z]+", "", line)
    racer_run = re.findall(r"\d", line)
    racer_distance = sum(int(digit) for digit in racer_run)


    if racer_name in participants:
        results[racer_name] = results.get(racer_name, 0) + racer_distance

sorted_results = sorted(results.items(), key=lambda x: -x[1])

suffixes = {1: "st", 2: "nd", 3: "rd"}
for i in range(min(3, len(sorted_results))):
    place = i + 1
    suffix = suffixes.get(place, "th")
    print(f'{place}{suffix} place: {sorted_results[i][0]}')
