import sqlite3
import json


def movie_on_title(title):
    dict_of_result = {}
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f"SELECT title, country, release_year, listed_in, description FROM netflix "
                 f"WHERE title = '{title}'"
                 f"ORDER BY release_year DESC")
        cursor.execute(query)
        data = cursor.fetchone()
        dict_of_result['title'] = f"{data[0]}"
        dict_of_result['country'] = f"{data[1]}"
        dict_of_result['release_year'] = f"{data[2]}"
        dict_of_result['listed_in'] = f"{data[3]}"
        dict_of_result['description'] = f"{data[4]}"
    return dict_of_result


def movie_between_years(year_1, year_2):
    data_list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f"SELECT title, release_year FROM netflix "
                 f"WHERE release_year BETWEEN '{year_1}' AND '{year_2}'"
                 f"LIMIT 100")
        cursor.execute(query)
        data = cursor.fetchall()
        for movie in data:
            dict_of_result = {'title': movie[0], 'release_year': movie[1]}
            data_list.append(dict_of_result)
    return data_list


def movie_rating(rating):
    data_list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        if rating == 'children':
            query = (f"SELECT title, rating, description FROM netflix "
                     f"WHERE rating = 'G'"
                     f"LIMIT 100")
        elif rating == 'family':
            query = (f"SELECT title, rating, description FROM netflix "
                     f"WHERE rating IN ('G', 'PG', 'PG-13')"
                     f"LIMIT 100")
        elif rating == 'adult':
            query = (f"SELECT title, rating, description FROM netflix "
                     f"WHERE rating IN ('R', 'NC-17')"
                     f"LIMIT 100")
        cursor.execute(query)
        data = cursor.fetchall()
        for movie in data:
            dict_of_result = {'title': movie[0], 'rating': movie[1], 'description': movie[2]}
            data_list.append(dict_of_result)
    return data_list


def movie_genre_to_json(genre):
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f"SELECT * FROM netflix "
                 f"WHERE listed_in LIKE '%{genre}%'"
                 f"ORDER BY release_year DESC "
                 f"LIMIT 10")
        cursor.execute(query)
        data = cursor.fetchall()
    return json.dumps(data)


def movie_genre(genre):
    data_list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f"SELECT title, description FROM netflix "
                 f"WHERE listed_in LIKE '{genre}'"
                 f"LIMIT 10")
        cursor.execute(query)
        data = cursor.fetchall()
        for movie in data:
            dict_of_result = {'title': movie[0], 'description': movie[1]}
            data_list.append(dict_of_result)
    return data_list


def two_actor(actor_1, actor_2):
    actors_list = []
    result = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = 'SELECT DISTINCT "cast" FROM netflix'
        cursor.execute(query)
        data = cursor.fetchall()
        for actors in data:
            if (actor_1 and actor_2) in actors[0]:
                actors_l = actors[0].split(', ')
                for actor in actors_l:
                    if actor not in (actor_1, actor_2):
                        actors_list.append(actor)
                for actor in actors_list:
                    if actors_list.count(actor) > 2 and actor not in result:
                        result.append(actor)
    return json.dumps(result)


def movie_type_year_genre(type_, year, genre):
    data_list = []
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = (f"SELECT title, description FROM netflix "
                 f"WHERE type = '{type_.title()}' AND release_year = '{year}'AND listed_in ='{genre.title()}' "
                 f"LIMIT 100")
        cursor.execute(query)
        data = cursor.fetchall()
        for movie in data:
            dict_of_result = {'title': movie[0], 'description': movie[1]}
            data_list.append(dict_of_result)

    return json.dumps(data_list)


# print(movie_type_year_genre('Movie', 2020, 'Dramas'))
# print(two_actor('Ben Lamb', 'Rose McIver'))
# print(movie_genre('DRAMAS'))
# print(movie_between_years(2001, 2002))
# print(movie_on_title('Bling Empire'))
