import math
import copy


def get_degrees(graph):
    degrees = {}

    for i, row in enumerate(graph):
        degree = sum(row)
        if degree > 0:
            degrees.setdefault(degree, [])
            degrees[degree].append(i)

    return degrees


def get_list_of_edges(graph):
    edges = {}

    for i, row in enumerate(graph):
        for j in range(i, len(row)):
            if row[j]:
                edges.setdefault(i, [])
                edges.setdefault(j, [])
                edges[i].append((i, j))
                edges[j].append((j, i))

    return edges


def is_all_disconnected(graph):
    for row in graph:
        degree = sum(row)

        if degree > 0:
            return False

    return True


def remove_vertex(graph, vertex):
    graph[vertex] = [False for _ in range(len(graph))]
    for row in graph:
        row[vertex] = False


def get_neighbours(graph, vertex):
    N = []

    for i, value in enumerate(graph[vertex]):
        if value:
            N.append(i)
    return N


def get_vc_of_simple_cycle(edges, k):
    min_vc = math.ceil(len(edges.keys())/2)

    if k < min_vc:
        return [-1]

    covered_edges = set()
    vc = set()
    current_vertex = list(edges.keys())[0]
    vc.add(current_vertex)
    min_vc -= 1

    while min_vc:
        next_edge = edges[current_vertex][0]
        if next_edge in covered_edges:
            next_edge = edges[current_vertex][1]

        covered_edges.add(next_edge)

        next_vertex = next_edge[1]
        next_vertex_edges = edges[next_vertex]

        for _, v in next_vertex_edges:
            if v not in vc:
                vc.add(v)
                min_vc -= 1
                current_vertex = v

    return list(vc)


def get_vc_of_pseudo_tree(graph, degrees, edges, k, f):
    one_deg_vertex = degrees[1][0]
    parent = edges[one_deg_vertex][0][1]

    remove_vertex(graph, parent)

    vc_ = f(graph, k-1)
    if (len(vc_) > k-1) or (len(vc_) > 0 and vc_[0] == -1):
        return [-1]
    vc = [parent] + vc_

    return vc


def vertex_cover_1(graph, k):
    n = len(graph)
    if k > n:
        return [-1]

    degrees = get_degrees(graph)
    edges = get_list_of_edges(graph)

    if is_all_disconnected(graph) or (len(edges) == 0 and k == 0):
        return []

    if 2 in degrees and len(degrees) == 1:
        return get_vc_of_simple_cycle(edges, k)

    if 1 in degrees:
        return get_vc_of_pseudo_tree(graph, degrees, edges, k, vertex_cover_1)

    n_high_degrees = len([key for key in degrees if key > 2])

    if n_high_degrees > 0:
        current_vertex = list(edges.keys())[0]
        remove_vertex(graph, current_vertex)

        vc_ = vertex_cover_1(graph, k-1)
        if ((0 < len(vc_) <= k-1) and vc_[0] != -1) or len(vc_) == 0:
            return [current_vertex] + vc_

        return [-1]

    return [-1]


def vertex_cover_3(graph, k):
    n = len(graph)
    if k > n:
        return [-1]

    degrees = get_degrees(graph)
    edges = get_list_of_edges(graph)

    if is_all_disconnected(graph) or (len(edges) == 0 and k == 0):
        return []

    if 2 in degrees and len(degrees) == 1:
        return get_vc_of_simple_cycle(edges, k)

    if 1 in degrees:
        return get_vc_of_pseudo_tree(graph, degrees, edges, k, vertex_cover_3)

    n_high_degrees = len([key for key in degrees if key > 2])

    if n_high_degrees > 0:
        current_vertex = list(edges.keys())[0]
        neighbours = get_neighbours(graph, current_vertex)
        n_neighbours = len(neighbours)

        for neighbour in neighbours:
            remove_vertex(graph, neighbour)

        vc_ = vertex_cover_3(graph, k-n_neighbours)
        if (len(vc_) > k-n_neighbours) or (len(vc_) > 0 and vc_[0] == -1):
            return [-1]

        vc = neighbours + vc_
        return vc

    return [-1]


def vertex_cover(graph, k):
    # n = len(graph)
    # if k > n:
    #     return [-1]

    degrees = get_degrees(graph)
    edges = get_list_of_edges(graph)

    if is_all_disconnected(graph) or (len(edges) == 0 and k == 0):
        return []

    if 2 in degrees and len(degrees) == 1:
        return get_vc_of_simple_cycle(edges, k)

    if 1 in degrees:
        return get_vc_of_pseudo_tree(graph, degrees, edges, k, vertex_cover_1)

    n_high_degrees = len([key for key in degrees if key > 2])

    if n_high_degrees > 0:
        current_vertex = list(edges.keys())[0]
        graph_copy = copy.deepcopy(graph)
        remove_vertex(graph_copy, current_vertex)

        vc_ = vertex_cover(graph_copy, k-1)
        if ((0 < len(vc_) <= k-1) and vc_[0] != -1) or len(vc_) == 0:
            return [current_vertex] + vc_

        neighbours = get_neighbours(graph, current_vertex)
        n_neighbours = len(neighbours)

        for neighbour in neighbours:
            remove_vertex(graph, neighbour)

        vc_ = vertex_cover(graph, k-n_neighbours)
        if (len(vc_) > k-n_neighbours) or (len(vc_) > 0 and vc_[0] == -1):
            return [-1]

        vc = neighbours + vc_
        return vc


def find_vertex_cover(graph, k):
    n = len(graph)
    if k > n:
        return [-1]

    vc = vertex_cover(graph, k)

    if (len(vc) > 0 and vc[0] == -1) or len(vc) == k:
        return vc

    v = 0
    while len(vc) < k and v < n:
        if v not in vc:
            vc.append(v)

        v += 1

    return vc


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
    [True, False, True, True],
    [True, True, False, True],
    [True, True, True, False],
]

graph3 = [
    [False, True, True, False, True, False, False],
    [True, False, False, True, False, True, False],
    [True, False, False, True, False, False, False],
    [False, True, True, False, True, True, True],
    [True, False, False, True, False, False, False],
    [False, True, False, True, False, False, True],
    [False, False, False, True, False, True, False],
]

graph4 = [
    [False, True, True, True, True, True, False],
    [True, False, True, True, True, False, False],
    [True, True, False, True, False, True, True],
    [True, True, True, False, True, True, True],
    [True, True, False, True, False, True, True],
    [True, False, True, True, True, False, True],
    [False, False, True, True, True, True, False],
]

# vc = find_vertex_cover(graph2, k=3)

# print('vc', vc)


def main(input):
    output = find_vertex_cover(input[0], input[1])
    return output


if __name__ == '__main__':
    pass
    main(input)


# You can use this function to test your code locally.
def examples():
    # This graph is a path of length 3.
    # Its center is a vertex cover of a size 1.
    vc = find_vertex_cover([
        [False, True, False],
        [True, False, True],
        [False, True, False]
    ], k=1)
    assert vc == [1]
    print('vc', vc)

    # This graph is a clique with 3 vertices.
    # It does not have a vertex cover of a size 1.
    vc = find_vertex_cover([
        [False, True, True],
        [True, False, True],
        [True, True, False]
    ], k=1)
    assert vc == [-1]
    print('vc', vc)

    # This graph is a full bipartite graph with 4 vertices.
    # Each of its halves is a vertex cover of a size 2.
    vc = find_vertex_cover([
        [False, False, True, True],
        [False, False, True, True],
        [True, True, False, False],
        [True, True, False, False],
    ], k=2)
    print('vc', vc)

    assert sorted(vc) == [0, 1] or sorted(vc) == [2, 3]


# examples()
