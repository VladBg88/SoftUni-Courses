data = input().split()
counter_symbols = {}

for word in data:
    for symbol in word:
        if symbol not in counter_symbols:
            counter_symbols[symbol] = 0
        counter_symbols[symbol] += 1

for key, value in counter_symbols.items():
    print(f"{key} -> {value}")
