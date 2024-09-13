TAX_PRICE = {
    'juniors': {'trail': 5.50, 'cross-country': 8, 'downhill': 12.25, 'road': 20},
    'seniors': {'trail': 7, 'cross-country': 9.50, 'downhill': 13.75, 'road': 21.50}
}

number_of_juniors = int(input())
number_of_seniors = int(input())
type_of_trace = str.lower(input()).strip()
tag_juniors = 'juniors'
tag_seniors = 'seniors'
price_of_juniors = 0
price_of_seniors = 0

if tag_juniors in TAX_PRICE and type_of_trace in TAX_PRICE[tag_juniors]:
    price_of_juniors = TAX_PRICE[tag_juniors][type_of_trace]

if tag_seniors in TAX_PRICE and type_of_trace in TAX_PRICE[tag_seniors]:
    price_of_seniors = TAX_PRICE[tag_seniors][type_of_trace]

if type_of_trace == 'cross-country' and (number_of_juniors + number_of_seniors) >= 50:
    price_of_juniors *= 0.75
    price_of_seniors *= 0.75

total_sum = (number_of_seniors * price_of_seniors) + (number_of_juniors * price_of_juniors)
total_sum *= 0.95  # 5% charges

print(f"{total_sum:.2f}")
