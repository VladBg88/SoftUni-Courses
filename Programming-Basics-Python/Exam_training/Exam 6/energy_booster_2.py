# Constants for fruit prices
PRICES = {
    'Watermelon': {'small': 56, 'big': 28.7},
    'Mango': {'small': 36.66, 'big': 19.6},
    'Pineapple': {'small': 42.10, 'big': 24.80},
    'Raspberry': {'small': 20, 'big': 15.2}
}

# Input
fruit = input().strip()
set_size = input().strip()
number_of_sets = int(input())

# Calculate price per set
if fruit in PRICES and set_size in PRICES[fruit]:
    price_per_set = PRICES[fruit][set_size] * (2 if set_size == 'small' else 5)
    total_price = price_per_set * number_of_sets

    # Apply discounts
    if 400 <= total_price <= 1000:
        total_price *= 0.85
    elif total_price > 1000:
        total_price *= 0.5

    # Output
    print(f'{total_price:.2f} lv.')
else:
    print("Incorrect input!")
