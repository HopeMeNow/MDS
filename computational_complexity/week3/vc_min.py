def convert_to_adj_list(graph):
    adj_list = {}

    for i, row in enumerate(graph):
        for j, value in enumerate(row):
            if value:
                adj_list.setdefault(i, [])
                adj_list[i].append(j)

                adj_list.setdefault(j, [])
                adj_list[j].append(i)

    return adj_list


def min_vc(graph, n):
    # Initialize all vertices as not visited.
    visited = [False] * (n)

    # Consider all edges one by one
    for u in range(n):
        # An edge is only picked when
        # both visited[u] and visited[v]
        # are false
        if not visited[u]:
            # Go through all adjacents of u and
            # pick the first not yet visited
            # vertex (We are basically picking
            # an edge (u, v) from remaining edges.
            for v in graph[u]:
                if not visited[v]:
                    # Add the vertices (u, v) to the
                    # result set. We make the vertex
                    # u and v visited so that all
                    # edges from/to them would
                    # be ignored
                    visited[v] = True
                    visited[u] = True
                    break

    return visited


def find_vertex_cover(graph, k):
    adj_list = convert_to_adj_list(graph)
    return min_vc(adj_list, len(graph))


graph1 = [
    [False, False, True, False, True, True],
    [False, False, True, False, True, True],
    [True, True, False, False, True, True],
    [False, False, False, False, True, True],
    [True, True, True, True, False, False],
    [True, True, True, True, False, False],
]

graph2 = [
    [False, True, True, True],
    [True, False, True, False],
    [True, True, False, True],
    [True, False, True, False],
]

vc = find_vertex_cover(graph1, k=5)

print('vc', vc)
