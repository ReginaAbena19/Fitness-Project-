from flask import Blueprint, render_template
from src.youtube import youtube_utils

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


@views.route('/results')
def results():
    videos2 = youtube_utils.get_workout_results_from_youtube()
    return render_template("results.html", len=len(videos2), videos=videos2)
