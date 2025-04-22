world_record_seconds = float(input())
distance_meters = float(input())
time_seconds_swimming = float(input())

water_resistance = int(distance_meters / 15)
slowing = water_resistance * 12.5
real_time = time_seconds_swimming * distance_meters + slowing

if real_time < world_record_seconds:
    print(f'Yes, he succeeded! The new world record is {real_time:.2f} seconds.')
else:
    late = real_time - world_record_seconds
    print(f'No, he failed! He was {late:.2f} seconds slower.')
