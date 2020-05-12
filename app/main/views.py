from flask import render_template
from . import main


# your views go here i.e for home,about
@main.route("/")
def index():
    return "<h1>Hello World</h1>"


@main.route("/about")
def about():
    pass