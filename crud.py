""" CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db


#functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def create_rating(user, score, movie):
    """create and retrun a rating"""

    rating = Rating(user = user, score = score, movie = movie)

    db.session.add(rating)
    db.session.commit()

    return rating

def all_movies():
    """Return all movies."""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """get movies by id"""
    movie_by_id = Movie.query.get(movie_id)

    return movie_by_id


def all_users():
    """return all users"""
    return User.query.all()

def get_users_by_id(user_id):
    """get users by id"""
    
    user_by_id = User.query.get(user_id)
    return user_by_id



if __name__ == '__main__':
    from server import app
    connect_to_db(app)