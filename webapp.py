import os

from flask import Flask


def create_app():
    # Create the flask instance and configure the app's secret key and database
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Load the instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)

    # os.makedirs() ensures that app.instance_path exists. Flask doesn’t create
    # the instance folder automatically, but it needs to be created because
    # your project will create the SQLite database file there.
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app