"""Server for movie ratings app."""
from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!
@app.route('/')
def homepage():

    return render_template("homepage.html")



@app.route('/movies')
def movies():

    all_movies = crud.all_movies()

    return render_template('all_movies.html', movies=all_movies)



@app.route('/movies/<movie_id>')
def movie_details(movie_id):
    """return movie details"""
    
    details = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', details=details)

@app.route('/users')
def users():

    all_users = crud.all_users()

    return render_template('users.html', users=all_users)



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
