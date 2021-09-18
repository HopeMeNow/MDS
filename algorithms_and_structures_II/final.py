import math


def to_adjacency_list(similarities):
    adjacency_list = {}

    for pair in similarities:
        zero_el_set = adjacency_list.setdefault(pair[0], set())
        first_el_set = adjacency_list.setdefault(pair[1], set())

        if len(zero_el_set) > 0:
            for i in zero_el_set:
                first_el_set.add(i)
                i_th = adjacency_list.setdefault(i, set())
                i_th.add(pair[1])

        zero_el_set.add(pair[1])

        if len(first_el_set) > 0:
            for i in first_el_set:
                zero_el_set.add(i)
                i_th = adjacency_list.setdefault(i, set())
                i_th.add(pair[0])

        first_el_set.add(pair[0])

    return adjacency_list


def get_views(friends):
    views = {}

    for watched_films in friends:
        for film in watched_films:
            views.setdefault(film, 0)
            views[film] += 1
    return views


def recommendation(movies, similarities, friends):
    similarity_graph = to_adjacency_list(similarities)
    views = get_views(friends)

    best_recommendation = ('', -math.inf)

    for movie in movies:
        S = 0
        F_S = 0
        F = views.setdefault(movie, 0)
        similar_films = similarity_graph[movie]

        for similar_film in similar_films:
            S += views.setdefault(similar_film, 0)

        S = float(S)/len(similar_films)

        if S != 0:
            F_S = F/S

        if F_S > best_recommendation[1]:
            best_recommendation = (movie, F_S)

    return best_recommendation[0]


movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker"]
similarities = [["Parasite", "1917"],
                ["Parasite", "Jojo Rabbit"],
                ["Joker", "Ford v Ferrari"]]
friends = [
    ["Joker"],
    ["Joker", "1917"],
    ["Joker"],
    ["Parasite"],
    ["1917"],
    ["Jojo Rabbit", "Joker"]
]

assert recommendation(movies, similarities, friends) == '1917', 'Wrong answer'
