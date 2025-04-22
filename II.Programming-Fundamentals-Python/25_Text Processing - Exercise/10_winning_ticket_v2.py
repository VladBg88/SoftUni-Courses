import re

tickets = input().split(", ")
tickets = [ticket.strip() for ticket in tickets]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue

    symbols = ['@', '#', '$', '^']
    found_match = False

    for symbol in symbols:
        # Escape symbol to ensure it is treated literally
        escaped_symbol = re.escape(symbol)
        pattern = f"{escaped_symbol}{{6,}}"

        left_match = re.search(pattern, ticket[0:10])
        right_match = re.search(pattern, ticket[10:])

        if left_match and right_match:
            left_length = len(left_match.group())
            right_length = len(right_match.group())
            min_length = min(left_length, right_length)

            if min_length == 10:
                print(f'ticket "{ticket}" - {min_length}{symbol} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {min_length}{symbol}')

            found_match = True
            break

    if not found_match:
        print(f'ticket "{ticket}" - no match')
