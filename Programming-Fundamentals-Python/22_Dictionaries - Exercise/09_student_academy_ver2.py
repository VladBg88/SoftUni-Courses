number_of_entries = int(input())
all_students_grades = {}

for _ in range(number_of_entries):
    student = input()
    grade = float(input())

    # Append grade to the student's list, or initialize a new list
    all_students_grades.setdefault(student, []).append(grade)

for student, grades in all_students_grades.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
