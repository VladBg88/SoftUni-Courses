courses_dictionary = {}

while True:
    command = input()
    if command == 'end':
        break
    command = command.split(" : ")
    course_name, student_name = command

    if course_name not in courses_dictionary:
        courses_dictionary[course_name] = []
    courses_dictionary[course_name] += [student_name]

for courses in courses_dictionary:
    print(f"{courses}: {len(courses_dictionary[courses])}")
    for students in courses_dictionary[courses]:
        print(f"-- {students}")
