# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy is an ORM (Object Relational Mapping)
# It is a programming technique for converting data from tables to
# objects

# To connect with a database with SQLAlchemy, we need a connector and a
# connector string.
#
# The connectors/drivers available for each database are as follows:
#   1) MySQL - MySQL Connector Python
#   2) PostgreSQL - psycopg2
#   3) SQLLite - sqllite3
#
# The connection string contains the required information to help us
# connect to a specific database and authenticate.
# Structure: dialect[+driver]://user:password@hostname/dbname[?key=value]
# Example:
# 1) SQLLite: sqllite:///<database_name.db>
# 2) MySQL: mysql+mysqlconnector://root:<password>@localhost:3306/db_name
engine = create_engine(
    'mysql+mysqlconnector://{username}:{password}@localhost:3306/stock_portfolio',
    convert_unicode=True,
)

# Creating a database via code
# connection = engine.connect()
# engine.execute('CREATE DATABASE stock_portfolio')

# The session establishes and maintains conversations between our program
# and the database
# Note: It is the entry point for all queries
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    ),
)

# This is the base class for all declarative class definitions. Every time
# we define a model, we need to make sure that the model class has `Base`
# set as the parent class as it helps them connect to the database.
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # This command creates all the tables that are bound to the Base metadata
    Base.metadata.create_all(bind=engine)


def close_db(e=None):
    db_session.remove()
