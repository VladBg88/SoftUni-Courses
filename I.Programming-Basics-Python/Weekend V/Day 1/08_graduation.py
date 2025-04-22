name = input()
grade = 1
warning = 0
sum_grades = 0.0

while True:
    if warning > 1:
        print(f"{name} has been excluded at {grade} grade")
        break

    new_grade = float(input())

    if 4.00 <= new_grade <= 6.00:
        sum_grades += new_grade
        if grade == 12:
            print(f"{name} graduated. Average grade: {sum_grades / 12:.2f}")
            break
        grade += 1
    elif 2 <= new_grade < 4:
        warning += 1
