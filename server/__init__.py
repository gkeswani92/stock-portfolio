# coding: utf-8
import os

from flask import Flask
from server.database import init_db
from server.database import close_db
from server.views.auth import auth_bp
from server.views.index import index_bp
from server.views.portfolio import portfolio_bp


def create_app():
    # Create the flask instance and configure the app's secret key and database
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'stock_portfolio.sqlite'),
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

    init_db()

    # app.teardown_appcontext() tells Flask to call that function when cleaning
    # up after returning the response.
    app.teardown_appcontext(close_db)

    # Registering blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(portfolio_bp)
    app.register_blueprint(index_bp)

    return app
