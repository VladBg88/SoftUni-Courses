period = int(input())
doctors = 7
accepted_patients = 0
rejected_patients = 0

for i in range(1, period + 1):
    if i % 3 == 0:
        if rejected_patients > accepted_patients:
            doctors += 1

    clients = abs(int(input()))

    if doctors >= clients:
        accepted_patients += clients
    else:
        rejected_patients += (clients - doctors)
        accepted_patients += doctors


print(f'Treated patients: {accepted_patients}.')
print(f'Untreated patients: {rejected_patients}.')
