from flask import Flask, render_template
from utils import *


app = Flask(__name__)


@app.route('/movie/<title>')
def page_of_movie(title):
    return render_template('movie.html', data=movie_on_title(title))


@app.route('/movie/<year_1>/to/<year_2>')
def page_of_movie_between_years(year_1, year_2):
    return render_template('movie_for_years.html', data=movie_between_years(year_1, year_2))


@app.route('/movie/rating/<rating>')
def page_of_movie_rating(rating):
    return render_template('movie_for_rating.html', data=movie_rating(rating))


@app.route('/movie/genre/<genre>')
def page_of_movie_genre(genre):
    return render_template('movie_for_genre.html', data=movie_genre(genre))


if __name__ == '__main__':
    app.run(debug=True)
