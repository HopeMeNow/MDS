import math


def fastest_escape_length(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1
    maze[i][j] = 1
    result = math.inf
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            print('i, j', i, j)
            new_res = fastest_escape_length(maze, a, b)
            if new_res != math.inf:
                result = new_res
    maze[i][j] = 0
    print('result', result)
    return result+1


maze = [
    [0, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
]

print(fastest_escape_length(maze))
