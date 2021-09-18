import math


def fastest_escapes(maze, i=0, j=0):
    # (i, j) is the starting position
    # maze[x][y] = 0 <=> (x, y) cell is empty
    # maze[x][y] = 1 <=> (x, y) cell contains a wall
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    maze[i][j] = 1
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            new_res = fastest_escapes(maze, a, b)
            min_pathes = []
            for path in new_res:
                if len(min_pathes) == 0:
                    min_pathes.append(path)
                else:
                    if len(path) <= len(min_pathes[-1]):
                        if len(path) < len(min_pathes[-1]):
                            min_pathes.clear()
                        min_pathes.append(path)

            if len(new_res) > 0:
                for path in min_pathes:
                    result.append([(i, j), *path])
    maze[i][j] = 0
    return result


maze = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 1, 0]
]

print(fastest_escapes(maze))
