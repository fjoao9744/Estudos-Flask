from flask import Blueprint, render_template

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home_page():
    return render_template("index.html")


    