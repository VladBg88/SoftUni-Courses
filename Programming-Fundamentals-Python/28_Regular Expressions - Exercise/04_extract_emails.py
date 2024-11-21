import re

# Input string
text = input()

# Refined regex to validate the emails based on the requirements
pattern = r"\s((([a-zA-Z0-9]+)[\.\_\-a-z0-9]*)@([a-z\-]+)(\.[a-z]+)+)\b"

# Find all matches in the input text
matches = re.findall(pattern, text)

# Print valid email addresses
for email in matches:
    print(email[0])
