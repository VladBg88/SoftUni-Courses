name = input().strip()
grade = 1
warning = 0
sum_grades = 0.0

while True:
    try:
        new_grade = float(input())
        if new_grade < 0 or new_grade > 6:
            print("Invalid grade. Please enter a grade between 0 and 6.")
            continue
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    sum_grades += new_grade
    if new_grade < 4.00:
        warning += 1
    if warning == 2:
        print(f"{name} has been excluded at {grade - 1} grade")
        break
    if grade == 12:
        print(f"{name} graduated. Average grade: {sum_grades / 12:.2f}")
        break
    grade += 1
