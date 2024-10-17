def merge_strings(data, start, end):
    start = max(0, start)
    end = min(len(data) - 1, end)
    merged_string = ''.join(data[start:end + 1])
    data[start:end + 1] = [merged_string]


def divide_string(data, index, partitions):
    string = data[index]
    part_length = len(string) // partitions
    extra_chars = len(string) % partitions

    new_parts = []
    current_position = 0
    for i in range(partitions):
        extra = 1 if i < extra_chars else 0
        new_parts.append(string[current_position:current_position + part_length + extra])
        current_position += part_length + extra

    data[index:index + 1] = new_parts


def process_commands(data, commands):
    for command in commands:
        parts = command.split()

        if parts[0] == 'merge':
            start_index = int(parts[1])
            end_index = int(parts[2])
            merge_strings(data, start_index, end_index)

        elif parts[0] == 'divide':
            index = int(parts[1])
            partitions = int(parts[2])
            divide_string(data, index, partitions)

        elif command == "3:1":
            break

    return data



data = input().split()
commands = []

while True:
    command = input()
    if command == "3:1":
        break
    commands.append(command)

result = process_commands(data, commands)

print(' '.join(result))
