# coding: utf-8

import os

from flask import Flask
from database import init_db_command
from database import close_db

def create_app():
    # Create the flask instance and configure the app's secret key and database
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Load the instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)

    # os.makedirs() ensures that app.instance_path exists. Flask doesnt create
    # the instance folder automatically, but it needs to be created because
    # your project will create the SQLite database file there
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # app.teardown_appcontext() tells Flask to call that function when cleaning
    # up after returning the response.
    app.teardown_appcontext(close_db)

    # app.cli.add_command() adds a new command that can be called with the
    # flask command.
    # Example: >> flask init-db
    app.cli.add_command(init_db_command)

    return app