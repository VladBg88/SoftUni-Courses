company_users_dictionary = {}

while True:
    command = input()
    if command == 'End':
        break
    command = command.split(" -> ")
    company, employees_id = command

    if company not in company_users_dictionary:
        company_users_dictionary[company] = []
    if employees_id not in company_users_dictionary[company]:
        company_users_dictionary[company] += [employees_id]

for company, employee in company_users_dictionary.items():
    print(company)
    for user_id in employee:
        print(f"-- {user_id}")
