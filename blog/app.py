from flask import Flask

from blog.ext import configuration


def simple_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)

    return app


def create_app(**config):
    app = simple_app(**config)
    configuration.load_extensions(app)

    return app
