def can_escape(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return True
    maze[i][j] = 1
    result = False
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            new_branch = can_escape(maze, a, b)
            print('a, b', a, b)
            print('new_branch', new_branch)
            result = result or new_branch
    # maze[i][j] = 0
    return result


maze = [
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0]
]

print(can_escape(maze))
