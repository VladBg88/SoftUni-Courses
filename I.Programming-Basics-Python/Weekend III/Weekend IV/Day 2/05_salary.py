FACEBOOK = 150
SITE_NAME_FACEBOOK = 'facebook'
INSTAGRAM = 100
SITE_NAME_INSTAGRAM = 'instagram'
REDDIT = 50
SITE_NAME_REDDIT = 'reddit'

tabs = int(input())
salary = int(input())
fines_amount = 0

for _ in range(tabs):
    site_name = input().lower().strip()

    if site_name == SITE_NAME_FACEBOOK:
        fines_amount += FACEBOOK
    elif site_name == SITE_NAME_INSTAGRAM:
        fines_amount += INSTAGRAM
    elif site_name == SITE_NAME_REDDIT:
        fines_amount += REDDIT

    if fines_amount >= salary:
        break

if fines_amount >= salary:
    print("You have lost your salary.")
else:
    print(int(salary - fines_amount))
