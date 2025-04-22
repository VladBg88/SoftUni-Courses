from collections import deque


def find_kate_position(maze):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if maze[r][c] == 'k':
                return r, c
    return None  # If no starting position for Kate is found


def is_exit(maze, row, col):
    # Check if position is at the edge of the maze and has an open path
    return (row == 0 or row == len(maze) - 1 or col == 0 or col == len(maze[0]) - 1) and maze[row][col] == ' '


def bfs_longest_path_to_exit(maze, start_row, start_col):
    rows, cols = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start_row, start_col, 0)])  # (row, col, distance)
    visited = set((start_row, start_col))
    longest_exit_path = -1

    while queue:
        row, col, distance = queue.popleft()

        # Check if the current position is an exit
        if is_exit(maze, row, col):
            longest_exit_path = max(longest_exit_path, distance)

        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited:
                if maze[new_row][new_col] == ' ':
                    queue.append((new_row, new_col, distance + 1))
                    visited.add((new_row, new_col))

    return longest_exit_path


def kate_escape(maze):
    start_position = find_kate_position(maze)
    if not start_position:
        return "Kate cannot get out"  # No starting position

    start_row, start_col = start_position
    longest_path = bfs_longest_path_to_exit(maze, start_row, start_col)

    if longest_path == -1:
        return "Kate cannot get out"
    else:
        return f"Kate got out in {longest_path} moves"


# Input
n = int(input("Enter number of rows: "))
maze = [input().strip() for _ in range(n)]

# Output the result
print(kate_escape(maze))
