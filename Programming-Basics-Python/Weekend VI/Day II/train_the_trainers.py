STOP_STRING = 'Finish'

judges = int(input())
presentations_count = 0
presentations_grades_sum = 0

while True:
    presentation_name = input()
    if presentation_name == STOP_STRING:
        break

    presentations_count += 1
    current_presentation_grades_sum = 0

    for judge_count in range(judges):
        grade = float(input())
        current_presentation_grades_sum += grade

    average_grade = current_presentation_grades_sum / judges
    presentations_grades_sum += average_grade

    print(f"{presentation_name} - {average_grade:.2f}.")

print(f"Student's final assessment is {presentations_grades_sum / presentations_count:.2f}.")
