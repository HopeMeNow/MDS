import math
from functools import reduce


def fastest_escape_length(maze, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return 1
    maze[i][j] = 1
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:
            new_res = fastest_escape_length(maze, a, b)
            if new_res != math.inf:
                result.append(new_res + 1)
    maze[i][j] = 0
    return min(result) if result else math.inf

def fastest_escapes(maze, i=0, j=0):
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

def weighted_escape_length(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return w if maze[i][j] == 1 else 1
    init_maze = maze[i][j]
    maze[i][j] = 2
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] != 2:
            new_res = weighted_escape_length(maze, w, a, b)
            if new_res != math.inf:
                if maze[a][b] == 0:
                    result.append(new_res + 1)
                else:
                    result.append(new_res + w)
    maze[i][j] = init_maze
    return min(result) if result else math.inf


def my_lambda(arr, maze = [[0, 0, 0],[1, 1, 0],[1, 1, 0]], w = 0):
    print('arr', arr)

    def inner_lambda(pair, maze, w = 0):
        print('pair', pair)
        print('maze', maze)
        # return 1 if maze[pair[0]][pair[1]] == 0 else w

    return reduce(inner_lambda, arr)


def weighted_escapes(maze, w, i=0, j=0):
    n = len(maze)
    m = len(maze[0])
    if i == n - 1 and j == m - 1:
        return [[(i, j)]]
    init_maze = maze[i][j]
    maze[i][j] = 2
    result = []
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
        if 0 <= a < n and 0 <= b < m and maze[a][b] != 2:
            new_res = weighted_escapes(maze, w, a, b)
            if len(new_res) > 0:
                for path in new_res:
                    if maze[a][b] == 0:
                        result.append([(i, j), *path])
                    else:
                        result.append([(i, j), *path])
    maze[i][j] = init_maze
    weights = list(
        map(
            lambda arr: sum(
                1 if maze[pair[0]][pair[1]] == 0 else w for pair in arr
            ),
            result
        )
    )
    if not weights:
        return result

    min_indexes = [
        index for index, elem in enumerate(weights) if min(weights) == elem
    ]

    return [result[index] for index in min_indexes]


# some test code
if __name__ == "__main__":
    test_a = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 0]
    ]
    # should print 5
    # print(fastest_escape_length(test_a))
    # # should print 2
    # print(weighted_escape_length(test_a, 0))
    test_b = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    # should print inf
    # print(fastest_escape_length(test_b))
    # # should print 5
    # print(weighted_escape_length(test_b, 1))
    # # should print 6
    # print(weighted_escape_length(test_b, 2))

    test_c = [
        [0, 0, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    # print('fastest_escape_length test_c', fastest_escape_length(test_c))
    test_d = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0],
        [0, 1, 0]
    ]

    # # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]]
    # print(fastest_escapes(test_c))
    # # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2)]]
    # print(fastest_escapes(test_d))
    # # should print [[(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # print(fastest_escapes(test_a))
    # # should print []
    # print(fastest_escapes(test_b))
    # # should print [5, 5, 5, 5, 5, 5]
    # print(list(map(len, fastest_escapes([[0 for _ in range(3)] for _ in range(3)]))))

    # # should print [[(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]]
    # print(weighted_escapes(test_b, 0))
    # # should print [[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]]
    # # the order of the paths within the list might be different
    # print(weighted_escapes(test_b, 2))
