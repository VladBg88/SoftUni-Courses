budget = float(input())
number_of_series = int(input())
total_sum = 0

for _ in range(number_of_series):
    name_of_series = str(input())
    price_for_series = float(input())

    if name_of_series == 'Thrones':
        total_sum += price_for_series * 0.5
    elif name_of_series == 'Lucifer':
        total_sum += price_for_series * 0.6
    elif name_of_series == 'Protector':
        total_sum += price_for_series * 0.7
    elif name_of_series == 'TotalDrama':
        total_sum += price_for_series * 0.8
    elif name_of_series == 'Area':
        total_sum += price_for_series * 0.9
    else:
        total_sum += price_for_series

if budget >= total_sum:
    print(f'You bought all the series and left with {budget - total_sum:.2f} lv.')
elif total_sum > budget:
    print(f'You need {total_sum - budget:.2f} lv. more to buy the series!')
