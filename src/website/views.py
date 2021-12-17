from flask import Flask, Blueprint, render_template
from src.youtube import youtube_utils


views = Blueprint('views', __name__)


@views.route('/', methods=["POST", "GET"])
def home():
    return render_template("home.html")


@views.route('/results/<workout_type>')
def results(workout_type):
    videos = youtube_utils.get_workout_results_from_youtube(workout_type)
    return render_template("results.html", len=len(videos), videos=videos)
