from flask import Blueprint

yourmodule = Blueprint('yourmodule', __name__)


@yourmodule.route('/')
def yourmodule_main():
    return 'YourModule Blueprint'
