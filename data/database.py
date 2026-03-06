from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask import Flask
import os

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class = Base)

def init_db(app: Flask) -> None:
    """
    Initializes the connection between the Flask application and the database.
    The database URI must be specified in the environment variable as
    'SQLALCHEMY_DATABASE_URI'.

    Parameters
    ----------
    app: Flask
        The Flask application
    """

    app['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    db.init_app(app = app)

    with app.app_context():
        db.create_all()