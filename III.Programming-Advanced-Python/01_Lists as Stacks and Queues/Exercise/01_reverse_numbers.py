n = input().split()
reversed_list = []

while n:
    reversed_list.append(n.pop())

print(' '.join(reversed_list))
