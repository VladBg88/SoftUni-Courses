budget = int(input())

while True:
    spend = input()
    if spend == 'End':
        print('You bought everything needed.')
        exit()
    elif int(spend) > budget:
        print('You went in overdraft!')
        exit()

    budget -= int(spend)
