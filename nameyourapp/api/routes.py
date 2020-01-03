from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/')
def api_main():
    return 'API Blueprint'
