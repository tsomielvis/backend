# models/movie.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(20), nullable=False)  # Date in YYYY-MM-DD format
    reviews = db.relationship('Review', backref='movie', lazy=True)
