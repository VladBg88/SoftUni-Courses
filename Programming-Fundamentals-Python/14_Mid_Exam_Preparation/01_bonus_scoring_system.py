number_of_students = int(input())
total_lectures = int(input())
additional_bonus = int(input())
max_score = 0
best_student = 0

for student in range(number_of_students):
    student_attendances = int(input())
    student_total_bonus = student_attendances / total_lectures * (5 + additional_bonus)
    if student_total_bonus > max_score:
        max_score = student_total_bonus
        best_student = student_attendances

print(f'Max Bonus: {round(max_score)}.')
print(f'The student has attended {best_student} lectures.')
