from collections import deque

rows, cols = map(int, input().split())
lair = [list(input().rstrip()) for _ in range(rows)]
commands = deque(input().rstrip())

# ── locate the player ──
player = next((r, c) for r in range(rows) for c in range(cols) if lair[r][c] == 'P')

DIRS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
in_bounds = lambda r, c: 0 <= r < rows and 0 <= c < cols

def spread_bunnies(field):
    newborn = []
    for r in range(rows):
        for c in range(cols):
            if field[r][c] == 'B':
                for dr, dc in DIRS.values():
                    nr, nc = r + dr, c + dc
                    if in_bounds(nr, nc) and field[nr][nc] != 'B':
                        newborn.append((nr, nc))
    for r, c in newborn:
        field[r][c] = 'B'


won = dead = False
last_pos = player                   # cell that will be printed if we escape

while commands and not (won or dead):
    move = commands.popleft()
    pr, pc = player
    lair[pr][pc] = '.'              # leave the current cell
    last_pos = (pr, pc)             # remember where we were **before** the move

    dr, dc = DIRS[move]
    nr, nc = pr + dr, pc + dc

    if not in_bounds(nr, nc):
        won = True                  # outside the lair – no further checks
    else:
        if lair[nr][nc] == 'B':
            dead = True
        else:
            lair[nr][nc] = 'P'
        player = (nr, nc)           # update only if still inside

    spread_bunnies(lair)            # bunnies always multiply

    if not won and lair[player[0]][player[1]] == 'B':
        dead = True                 # bitten after the spread

# ── print result ──
print('\n'.join(''.join(row) for row in lair))
if won:
    print(f'won: {last_pos[0]} {last_pos[1]}')
else:
    print(f'dead: {player[0]} {player[1]}')
