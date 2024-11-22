import re
number_of_lines = int(input())

pattern = r"@#+[A-Z][A-Z-a-z0-9]{4,}[A-Z]@#+"
product_group = r"\d+"

for lines in range(number_of_lines):
    text = input()
    matches = re.search(pattern, text)

    if matches:
        group = len(re.findall(product_group, matches.group()))
        if group == 0:
            print("Product group: 00")
        else:
            print(f"Product group: {''.join(re.findall(product_group, text))}")
    else:
        print("Invalid barcode")
