year = int(input())

for next_year in range(year + 1, year + 100):
    if len(str(next_year)) == len(set(str(next_year))):
        print(next_year)
        break
