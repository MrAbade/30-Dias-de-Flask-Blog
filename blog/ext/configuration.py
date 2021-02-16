from flask import Flask
from dynaconf import FlaskDynaconf
from importlib import import_module


def load_extensions(app: Flask):
    extension_list = app.config.get('EXTENSIONS')
    for extension in extension_list:
        params = [app]
        if 'migration' in extension:
            params.append(app.db)
        module = import_module(extension)
        module.init_app(*params)


def init_app(app: Flask, **config):
    FlaskDynaconf(
        app,
        settings_files=['settings.toml', '.secrets.toml'],
        **config
    )
