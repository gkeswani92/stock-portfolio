# coding: utf-8

import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    # g is a special object that is unique for each request. It is used to store
    # data that might be accessed by multiple functions during the request. The
    # connection is stored and reused instead of creating a new connection if
    # get_db is called a second time in the same request.
    if 'db' not in g:
        g.db = sqlite3.connect(
            # current_app is another special object that points to the Flask application
            # handling the request. Since you used an application factory, there is no
            # application object when writing the rest of your code. get_db will be
            # called when the application has been created and is handling a request,
            # so current_app can be used.
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )

        # sqlite3.Row tells the connection to return rows that behave like dicts.
        # This allows accessing the columns by name.
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    # close_db checks if a connection was created by checking if g.db was set.
    # If the connection exists, it is closed
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    # open_resource() opens a file relative to the current path, which is
    # useful since you won’t necessarily know where that location is when
    # deploying the application later. get_db returns a database connection,
    # which is used to execute the commands read from the file.
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


# click.command() defines a command line command called init-db that calls
# the init_db function and shows a success message to the user.
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')