from flask_migrate import Migrate
from flask import Flask

from .database import DatabaseSingleton


def init_app(app: Flask, db: DatabaseSingleton):
    Migrate(app, db)
