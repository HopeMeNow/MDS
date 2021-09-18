# define helper functions if needed
# and put them in `imdb_helper_functions` module.
# you can import them and use here like that:
import imdb_helper_functions as hp
import aiohttp
import asyncio
import functools
import itertools
import pandas as pd
import numpy as np

def get_actors_by_movie_soup(cast_page_soup, num_of_actors_limit=None, movie_url=None, movies=None):
    cast_table = cast_page_soup.find('table', attrs={'class': 'cast_list'})

    actors_links = []

    if not cast_table:
        return actors_links

    for link in cast_table.select('tr > td:nth-child(2) > a'):
        actors_links.append((link.text.strip(), link['href']))

    if movie_url and movies is not None:
        hp.update_movies_hash(movie_url, actors_links, movies)

    if num_of_actors_limit and num_of_actors_limit > 0:
        return actors_links[:num_of_actors_limit]
    return actors_links


def get_movies_by_actor_soup(actor_page_soup, num_of_movies_limit=None, actor_name=None, actors=None):
    filmography = hp.get_filmography_soup(actor_page_soup)

    films_list = []

    if not filmography:
        return films_list

    for film in filmography.find_all('div', attrs={'class': 'filmo-row'}):
        fiml_info_text = film.text.split('\n')
        if not fiml_info_text[5]:
            films_list.append((
                fiml_info_text[4],
                film.find('a', text=fiml_info_text[4])['href']
            ))

    if actor_name and actors is not None:
        hp.update_hash(actor_name, films_list, actors, 'actors')

    if num_of_movies_limit and num_of_movies_limit > 0:
        return films_list[:num_of_movies_limit]
    return films_list


# Some helped functions need to be placed in this file to avoid cyclic dependencies
def get_neighbour_actors(soup_or_list, movie_url, movies, num_of_actors_limit):
    if isinstance(soup_or_list, list):
        if soup_or_list and num_of_actors_limit:
            return soup_or_list[:num_of_actors_limit]
        return soup_or_list
    else:
        return get_actors_by_movie_soup(soup_or_list, num_of_actors_limit, movie_url, movies)


def get_actor_movies(soup_or_list, actor_name, actors, num_of_movies_limit):
    if isinstance(soup_or_list, list):
        if soup_or_list and num_of_movies_limit:
            return soup_or_list[:num_of_movies_limit]
        return soup_or_list
    else:
        return get_movies_by_actor_soup(soup_or_list, num_of_movies_limit, actor_name, actors)


async def get_actor_neighbours_by_url(
    actor,
    session,
    actors,
    movies,
    num_of_actors_limit,
    num_of_movies_limit,
    verbose,
):
    actor_soup_or_movies = await hp.get_actor(actor, actors, session, verbose)
    actor_movies = get_actor_movies(actor_soup_or_movies, actor[0], actors, num_of_movies_limit)

    actor_movies_urls = hp.list_of_pairs_to_urls(actor_movies)
    actor_movies_urls = list(map(lambda url: url + 'fullcredits', actor_movies_urls))

    movies_soups_or_actors = await hp.get_movies_by_urls(actor_movies_urls, movies, session, verbose)
    neighbour_actors = []

    for index, soup_or_actors in enumerate(movies_soups_or_actors):
        neighbour_actors.append(
            get_neighbour_actors(soup_or_actors, actor_movies_urls[index], movies, num_of_actors_limit)
        )

    return list(set(functools.reduce(lambda a, b: a + b, neighbour_actors, [])))


async def get_movie_distance(
    actor_start_url, actor_end_url, num_of_actors_limit=None, num_of_movies_limit=None, max_depth=5, verbose=False
):
    graph, actors, movies = hp.restore_cache(['graph', 'actors', 'movies'])

    async with aiohttp.ClientSession() as session:
        start_actor_soup = await hp.get_soup_by_url(actor_start_url, session)
        end_actor_soup = await hp.get_soup_by_url(actor_end_url, session)
        start_actor_name = hp.get_actor_name_by_soup(start_actor_soup)
        end_actor_name = hp.get_actor_name_by_soup(end_actor_soup)

        if not start_actor_name or not end_actor_name:
            return float('inf')

        next_neighbours = await get_actor_neighbours_by_url(
            (start_actor_name, actor_start_url),
            session, actors, movies, num_of_actors_limit, num_of_movies_limit, verbose
        )

        distance = 1

        while True:
            if end_actor_name in hp.list_of_pairs_to_names(next_neighbours):
                return distance
            elif distance >= max_depth:
                return float('inf')
            else:
                neighbours = []
                if verbose:
                    print('next_neighbours', len(next_neighbours))

                for i, neighbour in enumerate(next_neighbours):
                    if verbose:
                        print('Current distance', distance)
                        print(f'{i} neighbours of {len(next_neighbours)}')

                    actor_neighbours = graph.get(neighbour[0])

                    if actor_neighbours and verbose:
                        print(f'get {neighbour[0]} neighbours from cache')

                    if not actor_neighbours:
                        if verbose:
                            print(f'get {neighbour[0]} neighbours from site')
                        actor_neighbours = await get_actor_neighbours_by_url(
                            neighbour, session, actors, movies, num_of_actors_limit, num_of_movies_limit, verbose
                        )

                        hp.update_graph(graph, neighbour[0], actor_neighbours)

                    if verbose:
                        print('actor_neighbours', len(actor_neighbours))

                    neighbours += actor_neighbours

                next_neighbours = neighbours
                distance += 1


async def get_movie_descriptions_by_actor_soup(actor_page_soup, session):
    movies = get_movies_by_actor_soup(actor_page_soup)

    descriptions = []

    for movie in movies:
        movie_soup = await hp.get_soup_by_url(movie[1], session)
        descr_soup = movie_soup.select('p[data-testid=plot] > span:last-child')

        if descr_soup:
            descriptions.append(descr_soup[0].text)

    return descriptions


# print(hp.test_get_actors_by_movie_soup(get_actors_by_movie_soup))
# print(hp.test_get_movies_by_actor_soup(get_movies_by_actor_soup))


async def save_distances(actors):
    comb = set(itertools.combinations(actors, 2))
    result_table = pd.DataFrame(
        data=[[float('inf')]*10]*10,
        index=hp.list_of_pairs_to_names(actors),
        columns=hp.list_of_pairs_to_names(actors),
    )
    np.fill_diagonal(result_table.values, 0)

    for index, pair in enumerate(comb):
        print(f'Find distance between {pair[0][0]} and {pair[1][0]}, {index + 1}/{len(comb)}')

        res = await get_movie_distance(
            pair[0][1],
            pair[1][1],
            max_depth=3,
            num_of_actors_limit=5,
            num_of_movies_limit=5,
            verbose=True,
        )

        result_table[pair[0][0]][pair[1][0]] = res

        print(f'Distance between {pair[0][0]} and {pair[1][0]} is {res}')

    print(result_table)

    result_table.to_csv('result_csv.csv')


async def save_words_for_actors(actors):
    async with aiohttp.ClientSession() as session:
        for actor in actors:
            actor_soup = await hp.get_soup_by_url(actor[1], session)
            descriptions = await get_movie_descriptions_by_actor_soup(actor_soup, session)
            filename = '_'.join(actor[0].split(' '))
            hp.save_to_json(descriptions, filename)


async def main():
    actors = [
        ('Dwayne Johnson', 'https://www.imdb.com/name/nm0425005/'),
        ('Chris Hemsworth', 'https://www.imdb.com/name/nm1165110/'),
        ('Robert Downey Jr.', 'https://www.imdb.com/name/nm0000375/'),
        ('Akshay Kumar', 'https://www.imdb.com/name/nm0474774/'),
        ('Jackie Chan', 'https://www.imdb.com/name/nm0000329/'),
        ('Bradley Cooper', 'https://www.imdb.com/name/nm0177896/'),
        ('Adam Sandler', 'https://www.imdb.com/name/nm0001191/'),
        ('Scarlett Johansson', 'https://www.imdb.com/name/nm0424060/'),
        ('Sofia Vergara', 'https://www.imdb.com/name/nm0005527/'),
        ('Chris Evans', 'https://www.imdb.com/name/nm0262635/')
    ]

    await save_distances(actors)
    await save_words_for_actors(actors)


asyncio.run(main())
