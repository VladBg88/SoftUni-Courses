period = int(input())
doctors = 7
three_days_period_accepted_patients = 0
three_days_period_rejected_clients = 0
total_accepted_clients = 0
total_rejected_clients = 0

for i in range(1, period + 1):
    if i % 3 == 0:
        if three_days_period_rejected_clients > three_days_period_accepted_patients:
            doctors += 1
        three_days_period_accepted_patients = 0
        three_days_period_rejected_clients = 0

    clients = int(input())

    if clients <= doctors:
        three_days_period_accepted_patients += clients
        total_accepted_clients += clients
    else:
        three_days_period_accepted_patients += doctors
        total_accepted_clients += doctors
        three_days_period_rejected_clients += (clients - doctors)
        total_rejected_clients += (clients - doctors)

print(f'Treated patients: {total_accepted_clients}.')
print(f'Untreated patients: {total_rejected_clients}.')
