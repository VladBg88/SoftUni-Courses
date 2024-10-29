side_size = float(input())
sheets_number = int(input())
total_area_needed = side_size * side_size * 6
our_sheets_total_area = 0

for sheet in range(1, sheets_number + 1):
    length = float(input())
    width = float(input())

    sheet_area = length * width
    if sheet % 3 == 0:
        sheet_area *= 0.75
    if sheet % 5 == 0:
        sheet_area = 0
    our_sheets_total_area += sheet_area


if our_sheets_total_area >= total_area_needed:
    percentage_of_left_paper = 100 * (our_sheets_total_area - total_area_needed) / our_sheets_total_area
    print("You've covered the gift box!")
    print(f"{percentage_of_left_paper:.2f}% wrap paper left.")
else:
    percentage_of_uncovered_box = 100 * (total_area_needed - our_sheets_total_area) / total_area_needed
    print("You are out of paper!")
    print(f"{percentage_of_uncovered_box:.2f}% of the box is not covered.")
