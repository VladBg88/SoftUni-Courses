exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

if exam_hour == arriving_hour:
    if exam_minutes - arriving_minutes == 0:
        print('On time')
    elif exam_minutes - arriving_minutes <= 30:
        print('On time')
        print(f'{exam_minutes - arriving_minutes} minutes before the start')

if exam_hour - arriving_hour == 1:
    if exam_minutes == 0:
        if 60 - arriving_minutes <= 30:
            print('On time')
            print(f'{60 - arriving_minutes} minutes before the start')
if exam_hour - arriving_hour == 1:
    if exam_minutes != 0:
        if exam_minutes + (60 - arriving_minutes) <= 30:
            print('On time')
            print(f'{exam_minutes + (60 - arriving_minutes)} minutes before the start')

