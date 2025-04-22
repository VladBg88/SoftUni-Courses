MONDAY = 12
TUESDAY = 12
WEDNESDAY = 14
THURSDAY = 14
FRIDAY = 12
SATURDAY = 16
SUNDAY = 16

day = str(input())

if day == "Monday" or day == "Tuesday" or day == "Friday":
    print(MONDAY)
if day == "Wednesday" or day == "Thursday":
    print(WEDNESDAY)
if day == "Saturday" or day == "Sunday":
    print(SUNDAY)
