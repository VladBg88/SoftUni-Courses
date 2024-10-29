from math import floor

biscuits_production_per_day = int(input())
number_of_workers = int(input())
competing_biscuits = int(input())
total_biscuits = 0

for day in range(1, 30 + 1):
    production_of_biscuits = floor(number_of_workers * biscuits_production_per_day)

    if day % 3 == 0:
        production_of_biscuits = floor(0.75 * production_of_biscuits)

    total_biscuits += production_of_biscuits

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competing_biscuits:
    percentage = (abs(competing_biscuits - total_biscuits) / competing_biscuits) * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
else:
    percentage = (abs(competing_biscuits - total_biscuits) / competing_biscuits) * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")
