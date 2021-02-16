from flask import Flask, Blueprint


def init_app(app: Flask):
    base_url = '/api/v1'

    from .index import model_of_view
    bp_model_of_view = Blueprint('model_of_view', __name__, url_prefix=f'{base_url}/model-of-view')
    model_of_view(bp_model_of_view)


    app.register_blueprint(bp_model_of_view)
