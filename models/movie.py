from app import db  # Ensure you're importing db from the app module

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(20), nullable=False)  # e.g., YYYY-MM-DD format
