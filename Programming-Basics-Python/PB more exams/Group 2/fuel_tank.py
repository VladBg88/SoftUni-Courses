fuel_type = str.lower(input())
litres_of_fuel = int(input())

if fuel_type not in ('Diesel', 'Gasoline', 'Gas', 'diesel', 'gasoline', 'gas'):
    print("Invalid fuel!")
    exit()

if litres_of_fuel >= 25:
    print(f"You have enough {fuel_type}.")
else:
    print(f"Fill your tank with {fuel_type}!")
