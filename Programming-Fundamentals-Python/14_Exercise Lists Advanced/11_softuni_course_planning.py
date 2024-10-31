def softuni_course_planning():
    schedule_of_lessons = input().split(', ')

    while True:
        command = input().split(':')
        if command[0] == 'course start':
            break

        if 'Add' == command[0]:
            if command[1] not in schedule_of_lessons:
                schedule_of_lessons.append(command[1])

        elif 'Insert' == command[0]:
            if command[1] not in schedule_of_lessons:
                schedule_of_lessons.insert(int(command[2]), command[1])

        elif 'Remove' == command[0]:
            if command[1] in schedule_of_lessons:
                lesson_index = schedule_of_lessons.index(command[1])
                if lesson_index + 1 < len(schedule_of_lessons):
                    if 'Exercise' in schedule_of_lessons[lesson_index + 1]:
                        schedule_of_lessons.pop(lesson_index + 1)
                schedule_of_lessons.remove(command[1])

        elif 'Swap' == command[0]:
            if command[1] in schedule_of_lessons and command[2] in schedule_of_lessons:

                lesson_one_index = schedule_of_lessons.index(command[1])

                lesson_two_index = schedule_of_lessons.index(command[2])

                # Swap lessons

                schedule_of_lessons[lesson_one_index], schedule_of_lessons[lesson_two_index] = schedule_of_lessons[
                    lesson_two_index], schedule_of_lessons[lesson_one_index]

                # Swap exercises if they exist

                if lesson_one_index + 1 < len(schedule_of_lessons) and schedule_of_lessons[
                    lesson_one_index + 1] == f"{command[1]}-Exercise":
                    moved_exercise = schedule_of_lessons.pop(lesson_one_index + 1)

                    schedule_of_lessons.insert(lesson_two_index + 1, moved_exercise)

                if lesson_two_index + 1 < len(schedule_of_lessons) and schedule_of_lessons[
                    lesson_two_index + 1] == f"{command[2]}-Exercise":
                    moved_exercise = schedule_of_lessons.pop(lesson_two_index + 1)

                    schedule_of_lessons.insert(lesson_one_index + 1, moved_exercise)

        elif 'Exercise' == command[0]:
            if command[1] in schedule_of_lessons:
                lesson_index = schedule_of_lessons.index(command[1])
                if lesson_index + 1 >= len(schedule_of_lessons) or schedule_of_lessons[
                    lesson_index + 1] != f"{command[1]}-Exercise":
                    schedule_of_lessons.insert(lesson_index + 1, f"{command[1]}-Exercise")
            else:
                schedule_of_lessons.append(command[1])
                schedule_of_lessons.append(f"{command[1]}-Exercise")
    n = 1
    for i, lesson in enumerate(schedule_of_lessons, 1):
        print(f"{i}.{lesson}")


softuni_course_planning()
