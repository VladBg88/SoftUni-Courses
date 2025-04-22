grades_from_2_to_2_99 = 0
grades_from_3_to_3_99 = 0
grades_from_4_to_4_99 = 0
grades_from_5_to_6 = 0
average_value = 0

students = int(input())

for i in range(1, students + 1):
    valuation = float(input())
    average_value += valuation

    if 2.00 <= valuation <= 2.99:
        grades_from_2_to_2_99 += 1
    elif 3.00 <= valuation <= 3.99:
        grades_from_3_to_3_99 += 1
    elif 4.00 <= valuation <= 4.99:
        grades_from_4_to_4_99 += 1
    elif 5.00 <= valuation <= 6.00:
        grades_from_5_to_6 += 1

percent_students = 100 / students
print(f'Top students: {percent_students * grades_from_5_to_6:.2f}%')
print(f'Between 4.00 and 4.99: {percent_students * grades_from_4_to_4_99:.2f}%')
print(f'Between 3.00 and 3.99: {percent_students * grades_from_3_to_3_99:.2f}%')
print(f'Fail: {percent_students * grades_from_2_to_2_99:.2f}%')
print(f'Average: {average_value / students:.2f}')
