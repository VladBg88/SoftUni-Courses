import re

visited_places = []
travel_points = 0
places = input()

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, places)

for match in matches:
    visited_places.append(match.group(2))  # Extract the content of the second capturing group

for place in visited_places:
    travel_points += len(place)

print(f"Destinations: {', '.join(visited_places)}")
print(f"Travel Points: {travel_points}")
