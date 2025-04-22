user_string = input()
unique_symbols = sorted(set(map(str, user_string)))

for symbol in unique_symbols:
    print(f"{symbol}: {user_string.count(symbol)} time/s")