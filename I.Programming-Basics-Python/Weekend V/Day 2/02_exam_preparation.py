allowed_low_points = int(input())
counter_low_points = 0
counter_exams = 0
counter_score = 0
last_exam = ""

while True:
    exam_name = str(input())

    if exam_name == "Enough":
        print(f"Average score: {counter_score / counter_exams:.2f}")
        print(f"Number of problems: {counter_exams}")
        print(f"Last problem: {last_exam}")
        break

    score = int(input())
    counter_score += score
    counter_exams += 1

    if score <= 4:
        counter_low_points += 1

    if counter_low_points == allowed_low_points:
        print(f"You need a break, {counter_low_points} poor grades.")
        break

    last_exam = exam_name
