# models/watchlist.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

watchlist_movies = db.Table('watchlist_movies',
    db.Column('watchlist_id', db.Integer, db.ForeignKey('watchlist.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
    db.Column('date_added', db.String(20), nullable=False)  # Date in YYYY-MM-DD format
)

class Watchlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movies = db.relationship('Movie', secondary=watchlist_movies, lazy='subquery')
