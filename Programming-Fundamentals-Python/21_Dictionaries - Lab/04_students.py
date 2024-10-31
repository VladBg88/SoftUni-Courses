dictionary_students = {}

while True:
    command = input()
    if command[0].islower():
        break

    data = command.split(':')
    student_name, student_id, course_name = data

    if student_name not in dictionary_students:
        dictionary_students[student_name] = {}

    dictionary_students[student_name]['student_id'] = student_id
    dictionary_students[student_name]['course_name'] = course_name

command = command.replace('_', ' ')
for student in dictionary_students:
    if dictionary_students[student]['course_name'] == command:
        print(f"{student} - {dictionary_students[student]['student_id']}")
