SEA_VACATION = 680
MOUNTAIN_VACATION = 499

available_sea_vacations = int(input())
available_mountain_vacations = int(input())
total_earning = 0

while True:
    name_of_pack = input()
    if name_of_pack == 'Stop':
        break

    if name_of_pack == 'sea':
        if available_sea_vacations == 0:
            continue
        available_sea_vacations -= 1
        total_earning += SEA_VACATION
    elif name_of_pack == 'mountain':
        if available_mountain_vacations == 0:
            continue
        available_mountain_vacations -= 1
        total_earning += MOUNTAIN_VACATION

    if available_mountain_vacations == 0 and available_sea_vacations == 0:
        print(f"Good job! Everything is sold.")
        break

print(f"Profit: {total_earning} leva.")
