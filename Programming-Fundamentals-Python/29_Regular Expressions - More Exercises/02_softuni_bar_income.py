import re

pattern = r"%(?P<customer>[A-Z][a-z]+)%[^\|\$\%\.]*<(?P<product>\w+)>[^\|\$\%\.]*\|(?P<count>\d+)\|[^\|\$\%\.0-9]*(?P<price>\d+\.?\d*)\$"

total_income = 0

while True:
    text = input()
    if text == "end of shift":
        print(f"Total income: {total_income:.2f}")
        break

    match = re.match(pattern, text)
    if match:
        customer = match.group("customer")
        product = match.group("product")
        count = int(match.group("count"))
        price = float(match.group("price"))

        total_price = count * price
        total_income += total_price

        print(f"{customer}: {product} - {total_price:.2f}")
