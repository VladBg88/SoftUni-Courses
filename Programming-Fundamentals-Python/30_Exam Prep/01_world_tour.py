traveling_stops = input()

while True:
    command = input()
    if command == "Travel":
        print(f"Ready for world tour! Planned stops: {traveling_stops}")
        break

    if command.startswith('Add Stop'):
        index, stop = int(command.split(":")[1]), command.split(":")[2]
        if index < len(traveling_stops):
            traveling_stops = traveling_stops[:index] + stop + traveling_stops[index:]
        print(traveling_stops)
    elif command.startswith('Remove Stop'):
        start_index, end_index = int(command.split(":")[1]), int(command.split(":")[2])
        if start_index < len(traveling_stops) and end_index < len(traveling_stops):
            traveling_stops = traveling_stops[:start_index] + traveling_stops[end_index + 1:]
        print(traveling_stops)
    elif command.startswith('Switch'):
        old_string, new_string = command.split(":")[1], command.split(":")[2]
        if old_string in traveling_stops:
            traveling_stops = traveling_stops.replace(old_string, new_string, 1)
        print(traveling_stops)