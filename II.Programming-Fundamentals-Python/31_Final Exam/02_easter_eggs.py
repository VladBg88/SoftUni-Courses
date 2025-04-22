import re


def find_hidden_eggs():
    text = input()

    pattern = r"[@#]+(?P<color>[a-z]{3,})[@#]+[^a-z0-9]*\/(?P<amount>\d+)\/"

    matches = re.finditer(pattern, text)

    for match in matches:
        color = match.group("color")
        amount = match.group("amount")
        print(f"You found {amount} {color} eggs!")


find_hidden_eggs()