name = input()
grade = 0
warning = 0
sum_grade = 0.0

while True:
    new_grade = float(input())
    if new_grade < 4.00:
        warning += 1
        if warning > 1:
            print(f"{name} has been excluded at {grade} grade")
            break

    if new_grade >= 4.00:
        grade += 1
        sum_grade += float(new_grade)
        if grade == 12:
            print(f"{name} graduated. Average grade: {sum_grade / 12:.2f}")
