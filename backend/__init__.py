import os

from flask import Flask
from flask_restful import Api

from backend.resources.entries import Entries


SQLITE = 'sqlite:///'
# DB_PATH = '/home/achung/Rekor/rekor-backend/rekor.db'


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    DB_PATH = os.path.join(app.root_path, '../rekor.db')
    app.config.from_mapping(
        SECRET_KEY='dev',

        SQLALCHEMY_DATABASE_URI=SQLITE + DB_PATH,
        # SQLALCHEMY_BINDS={'graphs': SQLITE+os.path.join(app.root_path, 'graphs.db')},
        SQLALCHEMY_ECHO=False,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    api = Api(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.before_first_request
    def create_tables():
        from backend.db import db
        db.init_app(app)
        db.create_all()

    api.add_resource(Entries, '/entries')

    return app
