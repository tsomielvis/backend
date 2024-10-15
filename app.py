from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'

# Initialize SQLAlchemy after the app configuration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define your models
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.String(20), nullable=False)  # e.g., YYYY-MM-DD format

@app.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{'id': movie.id, 'title': movie.title, 'release_date': movie.release_date} for movie in movies])

if __name__ == '__main__':
    app.run(debug=True)
