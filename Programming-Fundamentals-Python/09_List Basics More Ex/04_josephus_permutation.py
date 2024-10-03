suicide_list = input().split()
unlucky_guy = int(input())
killed_guys = []

for i in range(unlucky_guy, len(suicide_list), unlucky_guy):
    killed_guys.append(suicide_list[i])




