from flask import Blueprint


def model_of_view(bp_app: Blueprint):
    @bp_app.route('/', methods=['GET'])
    def list_model_of_view():
        ...


    @bp_app.route('/', methods=['POST'])
    def create_model_of_view():
        ...


    @bp_app.route('/', methods=['PATCH'])
    def update_model_of_view():
        ...


    @bp_app.route('/', methods=['DELETE'])
    def delete_model_of_view():
        ...
