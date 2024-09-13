import math

bakes_number = int(input())
sugar_total = 0
flour_total = 0
max_sugar = 0
max_flour = 0

for _ in range(bakes_number):
    sugar_consumed = int(input())
    flour_consumed = int(input())
    sugar_total += sugar_consumed
    if sugar_consumed > max_sugar:
        max_sugar = sugar_consumed
    flour_total += flour_consumed
    if flour_consumed > max_flour:
        max_flour = flour_consumed

needed_sugar = sugar_total / 950
needed_flour = flour_total / 750

print(f'Sugar: {math.ceil(needed_sugar)}')
print(f'Flour: {math.ceil(needed_flour)}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')
