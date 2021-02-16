from flask_login import LoginManager
from flask import Flask


def init_app(app:Flask):
    auth_manager = LoginManager(app)
    auth_manager.login_view = 'auth.login'
    auth_manager.refresh_view = 'auth.refresh'
