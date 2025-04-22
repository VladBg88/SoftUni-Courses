offers = input().split(", ")
offers = [int(x) for x in offers]
beggars_count = int(input())

beggars = [0] * beggars_count

for i in range(len(offers)):
    beggars[i % beggars_count] += offers[i]

print(beggars)
