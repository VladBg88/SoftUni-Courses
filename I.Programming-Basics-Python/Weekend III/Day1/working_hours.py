hour = int(input())
day = str(input())

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')

if day == 'Thursday' or day == 'Friday' or day == 'Saturday':
    if 10 <= hour <= 18:
        print('open')
    else:
        print('closed')

if day == 'Sunday':
    print('closed')

# if day != 'Monday' or day == 'Tuesday' or day == 'Wednesday':
#   if day != day == 'Thursday' or day == 'Friday' or day == 'Saturday':
#      print('closed')
