from project.config import config
from project.models import Genre, Director, Movie, User
from project.server import create_app, db

app = create_app(config)

if __name__ == '__main__':
    app.run()
