import re
total_calories = 0

text = input()
pattern = r"([#|])([a-zA-Z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d{1,4})\1"

matches = re.findall(pattern, text)
calories = sum(int(match[3]) for match in matches)
days_last = calories // 2000
print(f"You have food to last you for: {days_last} days!")

for match in matches:
    item = match[1]
    date = match[2]
    calories = match[3]
    print(f"Item: {item}, Best before: {date}, Nutrition: {calories}")
