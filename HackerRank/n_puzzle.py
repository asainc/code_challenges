# N Puzzle is a sliding blocks game that takes place on a k * k grid with ((k * k) - 1) tiles each numbered from 1 to N.
# Your task is to reposition the tiles to their proper order.

# Input Format

# The first line of the input contains an integer k, the size of the square grid. 
# k * k lines follow each line containing an integer I on the tile starting from the top left to bottom right. 
# The empty cell is represented by the number 0.

# N = (k * k) -1
# 0 <= I <= N

# Constraints

# 3 <= k <= 5

# Output Format

# The first line contains an integer, M, the number of moves your algorithm has taken to solve the N-Puzzle. M lines follow.
# Each line indicating the movement of the empty cell (0).

# A grid is considered solved if it is of the following configuration.

# 0 1 2
# 3 4 5
# 6 7 8
# Sample Input

# 3
# 0
# 3
# 8
# 4
# 1
# 7
# 2
# 6
# 5
# Sample Output

# 70
# RIGHT
# DOWN
# ...
# ...
# ...
# Explanation

# The board given as input is

# 0 3 8
# 4 1 7
# 2 6 5
# After RIGHT, the board's configuration is

# 3 0 8
# 4 1 7
# 2 6 5
# Task

# Print all the moves made from the given configuration to the final solved board configuration.

# Scoring

# On successfully solving the puzzle, your score will be k * k.

import heapq
import sys

# Directions for moving the blank (0)
DIRS = {
    "UP":    (-1, 0),
    "DOWN":  (1, 0),
    "LEFT":  (0, -1),
    "RIGHT": (0, 1),
}

def manhattan(board, k):
    """Heuristic: Manhattan distance of all tiles."""
    dist = 0
    for i in range(k):
        for j in range(k):
            val = board[i][j]
            if val != 0:
                target_x = val // k
                target_y = val % k
                dist += abs(i - target_x) + abs(j - target_y)
    return dist

def serialize(board):
    return tuple(tuple(row) for row in board)

def find_zero(board, k):
    for i in range(k):
        for j in range(k):
            if board[i][j] == 0:
                return i, j

def swap(board, x1, y1, x2, y2):
    new_board = [list(row) for row in board]
    new_board[x1][y1], new_board[x2][y2] = new_board[x2][y2], new_board[x1][y1]
    return new_board

def solve(board, k):
    target = [[(i * k + j) % (k * k) for j in range(k)] for i in range(k)]

    start = serialize(board)
    goal = serialize(target)

    pq = []
    heapq.heappush(pq, (manhattan(board, k), 0, start, board, []))

    visited = set([start])

    while pq:
        f, g, ser, cur, path = heapq.heappop(pq)

        if ser == goal:
            return path

        zx, zy = find_zero(cur, k)

        for move, (dx, dy) in DIRS.items():
            nx, ny = zx + dx, zy + dy
            if 0 <= nx < k and 0 <= ny < k:
                nxt = swap(cur, zx, zy, nx, ny)
                s = serialize(nxt)
                if s not in visited:
                    visited.add(s)
                    new_g = g + 1
                    h = manhattan(nxt, k)
                    heapq.heappush(pq, (new_g + h, new_g, s, nxt, path + [move]))

    return None

# ---------------------------
# Main Input / Output
# ---------------------------
data = sys.stdin.read().strip().split()
k = int(data[0])

vals = list(map(int, data[1:]))

board = []
idx = 0
for i in range(k):
    row = []
    for j in range(k):
        row.append(vals[idx])
        idx += 1
    board.append(row)

moves = solve(board, k)

print(len(moves))
for m in moves:
    print(m)
