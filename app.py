from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models here
from models.movie import Movie
from models.user import User
from models.watchlist import Watchlist

if __name__ == '__main__':
    app.run(debug=True)
