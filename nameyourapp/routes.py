from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def main_index():
    return '<div align="center"><img src="https://source.unsplash.com/1200x800/?hacker,IT,matrix,women"><p>Thanks Unsplash for nice photo</p></div>', 200
