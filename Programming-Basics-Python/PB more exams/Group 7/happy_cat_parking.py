total_days = int(input())
total_hours = int(input())
daily_total_price = 0
total_sum = 0

for days in range(1, total_days + 1):
    daily_total_price = 0
    for hours in range(1, total_hours + 1):
        if days % 2 == 0 and hours % 2 != 0:
            daily_price = 2.50
        elif days % 2 != 0 and hours % 2 == 0:
            daily_price = 1.25
        else:
            daily_price = 1

        daily_total_price += daily_price
        total_sum += daily_price

    print(f'Day: {days} - {daily_total_price:.2f} leva')

print(f'Total: {total_sum:.2f} leva')
