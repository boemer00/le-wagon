def detailed_movies(db):
    # return the list of movies with their genres and director name
    query = """
        SELECT movies.title, movies.genres, directors.name
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        """
    db.execute(query)
    results = db.fetchall()
    movies = []
    for movie in results:
        movies.append(movie)
    return movies

def top_five_youngest_newly_directors(db):
    # return the top 5 youngest directors when they direct their first movie
    query = """
        SELECT directors.name, (movies.start_year - directors.birth_year) AS age,
	    movies.title, movies.start_year, directors.birth_year
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        WHERE age IS NOT NULL
        ORDER BY age ASC
        LIMIT 5;
        """
    db.execute(query)
    results = db.fetchall()
    directors = []
    for direct in results:
        directors.append(direct[:2])
    return directors

def late_released_movies(db):
    # return the list of all movies released after their director death
    query = """
        SELECT movies.title, movies.start_year, directors.death_year
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        WHERE directors.death_year < movies.start_year;
        """
    db.execute(query)
    results = db.fetchall()
    movies = []
    for movie in results:
        movies.append(movie[0])
    return movies

def stats_on(db, genre_name):
    # return a dict of stats for a given genre
    query = f"""
        SELECT movies.genres, COUNT(movies.title), ROUND(AVG(movies.minutes),2)
        FROM movies
        WHERE movies.genres = '{genre_name}';
        """
    db.execute(query)
    results = db.fetchone()
    final_dict = {'genre': results[0], 'number_of_movies': results[1], 'avg_length': results[2]}
    return final_dict


def top_five_directors_for(db, genre_name):
    # return the top 5 of the directors with the most movies for a given genre
    query = f"""
            SELECT directors.name, COUNT(*) movie_count
            FROM movies
            JOIN directors ON movies.director_id = directors.id
            WHERE movies.genres = "{genre_name}"
            GROUP BY directors.name
            ORDER BY movie_count DESC, directors.name
            LIMIT 5;
            """
    db.execute(query)
    results = db.fetchall()
    return results


def movie_duration_buckets(db):
    # return the movie counts grouped by bucket of 30 min duration
    query = """
        SELECT
            (minutes / 30 + 1)*30 time_range,
            COUNT(*)
        FROM movies
        WHERE minutes IS NOT NULL
        GROUP BY time_range
    """
    return db.execute(query).fetchall()
