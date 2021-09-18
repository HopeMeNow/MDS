import requests
from bs4 import BeautifulSoup
import json
import urllib
import time


def list_of_pairs_to_names(list_of_tuples):
    zipped = list(zip(*list_of_tuples))
    return list(zipped[0]) if zipped else []

def list_of_pairs_to_urls(list_of_tuples):
    zipped = list(zip(*list_of_tuples))
    return list(zipped[1]) if zipped else []


def aggregate_urls_to_list(agg, list_of_tuples):
    return agg + list_of_pairs_to_urls(list_of_tuples)


graph = {
    'start': [('one', '/dfg/sdfg/'), ('two', '/sdfg/sdf/')],
    'one': [('start', '/sdfd/sdf'), ('two', '/sdfg/sdf/'), ('three', '/df/qwe/')],
    'two': [('start', '/sdfd/sdf'), ('one', '/dfg/sdfg/'), ('three', '/df/qwe/'), ('end', '/asdf/awsdf/')],
    'three': [('two', '/sdfg/sdf/'), ('end', '/asdf/awsdf/')],
    'end': [('two', '/sdfg/sdf/'), ('three', '/df/qwe/')],
}


def save_to_json(obj, filename):
    with open(f'{filename}.json', 'w') as f:
        json.dump(obj, f)


def update_graph(graph: dict, key: str, vertices: list):
    neighbours = graph.setdefault(key, [])
    neighbours += vertices

    save_to_json(graph, 'graph')


def update_movies_hash(url: str, value: list, hash_table: dict):
    key = url.split('/')[2]
    update_hash(key, value, hash_table, 'movies')


def update_hash(key: str, value: list, hash_table: dict, hash_name: str):
    current_values = hash_table.setdefault(key, [])
    set_values = set(current_values)
    set_values.update(value)
    current_values += list(set_values)

    save_to_json(hash_table, hash_name)


def get_actor_name_by_soup(soup):
    name_el = soup.select('h1.header > span.itemprop')
    name = ''

    if name_el:
        name = name_el[0].text.strip()

    return name

def to_list_of_tuples(array):
    return list(map(tuple, array))


def restore_cache(cache_names: list):
    data = []
    for name in cache_names:
        try:
            with open(f'{name}.json', 'r') as f:
                hash = dict(map(
                    lambda pair: (pair[0], to_list_of_tuples(pair[1])),
                    json.load(f).items()
                ))
                data.append(hash)
        except Exception:
            data.append({})
    return data


async def get_soup_by_url(url: str, session):
    full_url = urllib.parse.urljoin('https://www.imdb.com/', url)
    headers = {'Accept-Language': 'en', 'X-FORWARDED-FOR': '2.21.184.0'}
    async with session.get(full_url, headers=headers) as resp:
        time.sleep(0.01)
        page = await resp.text()
        return BeautifulSoup(page)


async def get_actor(actor, hash, session, verbose):
    actor_films = hash.get(actor[0])

    if actor_films:
        if verbose:
            print('Get actor from cache\n')
        return actor_films
    else:
        if verbose:
            print('Get actor from site\n')
        return await get_soup_by_url(actor[1], session)


async def get_movies_by_urls(urls: list, hash, session, verbose):
    soups = []
    for url in urls:
        try:
            movie_id = url.split('/')[2]
            movie_actors = hash.get(movie_id)
            if movie_actors:
                if verbose:
                    print('Get actors of movie from cache\n')
                soups.append(movie_actors)
            else:
                if verbose:
                    print('Get actors of movie from site\n')
                soups.append(await get_soup_by_url(url, session))
        except Exception:
            continue
    return soups


def get_filmography_soup(soup):
    filmography = soup.select(
        '#filmo-head-actor + .filmo-category-section'
    )

    if not filmography:
        filmography = soup.select(
            '#filmo-head-actress + .filmo-category-section'
        )

    return filmography[0] if filmography else None


def test_get_actors_by_movie_soup(function):
    headers = {'Accept-Language': 'en', 'X-FORWARDED-FOR': '2.21.184.0'}
    response = requests.get(
        'https://www.imdb.com/title/tt0120689/fullcredits',
        headers=headers
    )
    soup = BeautifulSoup(response.text)

    assert len(function(soup)) == 59
    assert function(soup, 2) == [
        ('Tom Hanks', '/name/nm0000158/'), ('David Morse', '/name/nm0001556/')
    ]
    assert len(function(soup, 0)) == 59
    assert len(function(soup, -3)) == 59
    return 'Tests successfully passed'


def test_get_movies_by_actor_soup(function):
    # male
    headers = {'Accept-Language': 'en', 'X-FORWARDED-FOR': '2.21.184.0'}
    response = requests.get(
        'https://www.imdb.com/name/nm0000158',
        headers=headers
    )
    soup = BeautifulSoup(response.text)

    assert len(function(soup)) == 58
    assert function(soup, 2) == [
        ('News of the World', '/title/tt6878306/'),
        ('Borat Subsequent Moviefilm', '/title/tt13143964/')
    ]
    assert len(function(soup, 0)) == 58
    assert len(function(soup, -3)) == 58

    # female
    headers = {'Accept-Language': 'en', 'X-FORWARDED-FOR': '2.21.184.0'}
    response = requests.get(
        'https://www.imdb.com/name/nm0001073',
        headers=headers
    )
    soup = BeautifulSoup(response.text)
    assert len(function(soup)) == 24
    assert function(soup, 2) == [
        ('Mothers and Daughters', '/title/tt2395339/'),
        ('Scream 4', '/title/tt1262416/')
    ]
    assert len(function(soup, 0)) == 24
    assert len(function(soup, -3)) == 24

    return 'Tests successfully passed'
