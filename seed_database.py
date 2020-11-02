"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')
# More code will go here

#connect to database
model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as files:
    movie_data = json.loads(files.read())

movies_in_db = []
for movie in movie_data:
    title = movie['title']
    overview = movie['overview']
    poster_path = movie['poster_path']
    release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
    movie1 = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(movie1)


for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user = crud.create_user(email, password)

    for u in range(10):
        score = randint(1, 5)
        movie_random = choice(movies_in_db)
        

        rating = crud.create_rating(user, score, movie_random)