city = str(input())
sales = float(input())
commissions = 0.00

if city == 'Sofia':
    if 0 <= sales <= 500:
        commissions = 0.05
    if 500 < sales <= 1000:
        commissions = 0.07
    if 1000 < sales <= 10000:
        commissions = 0.08
    if sales > 10000:
        commissions = 0.12

if city == 'Varna':
    if 0 <= sales <= 500:
        commissions = 0.045
    if 500 < sales <= 1000:
        commissions = 0.075
    if 1000 < sales <= 10000:
        commissions = 0.10
    if sales > 10000:
        commissions = 0.13

if city == 'Plovdiv':
    if 0 <= sales <= 500:
        commissions = 0.055
    if 500 < sales <= 1000:
        commissions = 0.08
    if 1000 < sales <= 10000:
        commissions = 0.12
    if sales > 10000:
        commissions = 0.145

if (city == 'Sofia' or city == 'Plovdiv' or city == 'Varna') and sales >= 0.01:
    print(f"{commissions * sales:.2f}")
else:
    print('error')
