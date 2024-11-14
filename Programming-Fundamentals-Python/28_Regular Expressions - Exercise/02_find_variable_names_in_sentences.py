import re

text = input()

pattern = r"(?<=\b_)[a-zA-Z0-9]+\b(?!_)"

match_variable_names = re.findall(pattern, text)

print(",".join(match_variable_names))
