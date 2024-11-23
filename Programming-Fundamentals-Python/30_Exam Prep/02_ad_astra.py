import re
food_items = []
total_calories = 0

text = input()
pattern = r"([#|])(?P<item>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,4})\1"

matches = re.finditer(pattern, text)
for match in matches:
    item = match.group("item")
    date = match.group("date")
    calories = int(match.group("calories"))
    food_items.append((item, date, calories))
    total_calories += calories

days_last = total_calories // 2000
print(f"You have food to last you for: {days_last} days!")

for item, date, calories in food_items:
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
