import os

from flask import Flask
from flask_restful import Api

from backend.resources.entries import Entries


DB_PATH = os.path.join(__file__, '../../rekor.db')
DB_URI = 'sqlite:///' + DB_PATH
DB_ROOT_PSSWD = os.getenv('DB_ROOT_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
if DB_ROOT_PSSWD and DB_HOST and DB_NAME:
    DB_URI = f"mariadb://root:{DB_ROOT_PSSWD}@{DB_HOST}:3306/{DB_NAME}"


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',

        SQLALCHEMY_DATABASE_URI=DB_URI,
        # SQLALCHEMY_BINDS={'graphs': SQLITE+os.path.join(app.root_path, 'graphs.db')},
        SQLALCHEMY_ECHO=False,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    print(DB_URI, flush=True)

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
        try:
            db.init_app(app)
            db.create_all()
        except Exception as exception:
            print(exception)

    api.add_resource(Entries, '/entries')

    return app
