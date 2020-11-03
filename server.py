# """  """"""Server for movie ratings app."""

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

@app.route('/users/<user_id>')
def user_detial(user_id):

    user_details = crud.get_users_by_id(user_id)

    return render_template('user_profile.html', user_details=user_details)

@app.route('/users', methods=['POST'])
def create_account():

    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user is None:
        user = crud.create_user(email, password)
        flash('Account created! Now log in.')
        return redirect('/')
    else:
        flash("User already exists. Please try again...")
        return redirect('/')

    
