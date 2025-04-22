number_of_entries = int(input())
all_students_grades = {}
final_students_grades = {}

for i in range(number_of_entries):

    student = input()
    grade = float(input())

    if student not in all_students_grades:
        all_students_grades[student] = [grade]
    else:
        all_students_grades[student].append(grade)

for student, grades in all_students_grades.items():
    average_grades = sum(grades) / len(grades)

    if average_grades >= 4.50:
        final_students_grades[student] = average_grades
        print(f"{student} -> {average_grades:.2f}")
