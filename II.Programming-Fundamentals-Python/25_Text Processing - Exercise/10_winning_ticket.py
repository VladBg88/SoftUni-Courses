from itertools import count

tickets = input().split(", ")
tickets = [word.strip() for word in tickets]

for ticket in tickets:
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    elif ticket[0:10].count('@') >= 6 and ticket[10:20].count('@') >= 6:
        first_half = ticket[0:10].count('@')
        second_half = ticket[10:20].count('@')
        if first_half + second_half == 20:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}@ Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}@")
    elif ticket[0:10].count('#') >= 6 and ticket[10:20].count('#') >= 6:
        first_half = ticket[0:10].count('#')
        second_half = ticket[10:20].count('#')
        if first_half + second_half == 20:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}@ Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}#")
    elif ticket[0:10].count('$') >= 6 and ticket[10:20].count('$') >= 6:
        first_half = ticket[0:10].count('$')
        second_half = ticket[10:20].count('$')
        if first_half + second_half == 20:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}$ Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}$")
    elif ticket[0:10].count('^') >= 6 and ticket[10:20].count('^') >= 6:
        first_half = ticket[0:10].count('^')
        second_half = ticket[10:20].count('^')
        if first_half + second_half == 20:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}@ Jackpot!")
        else:
            print(f"ticket \"{ticket}\" - {min(first_half, second_half)}^")
    else:
        print(f"ticket \"{ticket}\" - no match")
