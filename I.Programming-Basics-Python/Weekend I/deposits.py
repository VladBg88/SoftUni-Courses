deposit = float(input())
period = int(input())
percentage = float(input()) / 100

money_in_the_bank = deposit + period * ((deposit * percentage) / 12)

print(money_in_the_bank)