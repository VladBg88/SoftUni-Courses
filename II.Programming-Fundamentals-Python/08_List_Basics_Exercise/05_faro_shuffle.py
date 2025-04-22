cards = input().split()
n_shuffles = int(input())

for _ in range(n_shuffles):
    half = len(cards) // 2
    left_half = cards[:half]
    right_half = cards[half:]

    shuffled_deck = []
    for i in range(half):
        shuffled_deck.append(left_half[i])
        shuffled_deck.append(right_half[i])
    cards = shuffled_deck

print(cards)
