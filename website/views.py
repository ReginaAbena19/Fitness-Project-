from flask import Blueprint, render_template

views = Blueprint('views', __name__)
videos = ["glxrwC9zsHY",
          "oo9s2zg_nC4",
          "-b2lNLq3EaA"]


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/results')
def results():
    return render_template("results.html", len=len(videos), videos=videos)
