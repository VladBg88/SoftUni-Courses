old_record = float(input())
distance = float(input())
one_meter_time = float(input())

slowing = (distance // 50) * 30
new_record = one_meter_time * distance + slowing

if new_record < old_record:
    print(f'Yes! The new record is {new_record:.2f} seconds.')
else:
    print(f'No! He was {new_record - old_record:.2f} seconds slower.')
