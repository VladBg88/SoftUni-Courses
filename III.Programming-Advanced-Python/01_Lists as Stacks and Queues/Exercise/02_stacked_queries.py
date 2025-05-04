from collections import deque

stacked_queries = deque()
number_of_operations = int(input())

for operation in range(number_of_operations):
    command_line = [int(x) for x in input().split()]
    if len(command_line) > 1 and command_line[0] == 1:
        stacked_queries.appendleft(command_line[1])
    elif command_line[0] == 2:
        try:
            stacked_queries.popleft()
        except IndexError:
            continue
    elif command_line[0] == 3:
        if stacked_queries:
            print(max(stacked_queries))
    elif command_line[0] == 4:
        if stacked_queries:
            print(min(stacked_queries))

print(', '.join(map(str, stacked_queries)))
