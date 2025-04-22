pages = int(input())
pages_per_hour = int(input())
days = int(input())

all_time = pages // pages_per_hour
hours_per_day = all_time // days

print(hours_per_day)