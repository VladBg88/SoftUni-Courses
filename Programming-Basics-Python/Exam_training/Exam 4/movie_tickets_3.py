a1 = int(input())
a2 = int(input())
n = int(input())

for symbol1 in range(a1, a2):
    char_symbol1 = chr(symbol1)
    if symbol1 % 2 == 1:  # ASCII of Symbol 1 should be odd
        for symbol2 in range(1, n):
            for symbol3 in range(1, n // 2):
                symbol4 = symbol1  # ASCII code of Symbol 1
                if (symbol2 + symbol3 + symbol4) % 2 == 1:  # Sum should be odd
                    ticket = f"{char_symbol1}-{symbol2}{symbol3}{symbol4}"
                    print(ticket)
