def softuni_reception():
    first_employee_efficiency = int(input())  # students per hour efficiency
    second_employee_efficiency = int(input())  # students per hour efficiency
    third_employee_efficiency = int(input())  # students per hour efficiency

    students_count = int(input())
    hour = 1
    all_horse_power = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency

    while students_count > 0:
        if hour % 4 == 0:
            hour += 1
            continue

        students_count -= all_horse_power
        hour += 1

    print(f"Time needed: {hour - 1}h.")

softuni_reception()
