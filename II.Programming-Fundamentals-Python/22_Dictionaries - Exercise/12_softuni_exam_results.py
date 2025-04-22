database_of_exams = {}
counter_submissions = {}

while True:
    banned = False
    command = input()
    if command == 'exam finished':
        break
    command = command.split('-')
    if len(command) == 2:
        username = command[0]
        banned = True
    elif len(command) == 3:
        username, language, points = command[0], command[1], int(command[2])
    else:
        print('Wrong input!')
        continue

    if banned:
        if username in database_of_exams:
            del database_of_exams[username]
        continue

    if username not in database_of_exams:
        database_of_exams[username] = {language: points}
    else:
        if username in database_of_exams and language in database_of_exams[username]:
            if points > database_of_exams[username][language]:
                database_of_exams[username][language] = points

    if language in counter_submissions:
        counter_submissions[language] += 1
        continue
    counter_submissions[language] = 1


print('Results:')
for usernames, languages in database_of_exams.items():
    for language, points in languages.items():
        print(f"{usernames} | {points}")
print('Submissions:')
for languages, points in counter_submissions.items():
    print(f"{languages} - {points}")
