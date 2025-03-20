from collections import deque

participants = deque(input().split())
n_toss = int(input()) - 1

while len(participants) > 1:
    participants.rotate(-n_toss)
    removed_kid = participants.popleft()
    print(f"Removed {removed_kid}")

print(f"Last is {participants.pop()}")