from flask import Blueprint, render_template, request, session
from src.website.quiz.written_workout import WrittenWorkout
from werkzeug.utils import redirect

from src.website.youtube.youtube_utils import YoutubeWorkout

views = Blueprint('views', __name__)

"""
This file creates the routes for the home page and the results page. 
"""
@views.route('/', methods=["POST", "GET"])
def home():
    if session:
        return render_template("home.html")
    else:
        return redirect('/login')


@views.route('/results/', methods=["POST", "GET"])
def results():
    workout_type = request.form['workout-location'] + "+" + request.form['muscle-group'] + "+" + "workout"
    workout_specified = request.form['submit-button']
    if workout_specified == "written":
        written_workout = WrittenWorkout()
        return written_workout.get_written_workout()
    elif workout_specified == "personalised-youtube":
        youtube_workout = YoutubeWorkout(workout_type, 3)
        return youtube_workout.get_workout_results_from_youtube(workout_type, 3)
    elif workout_specified == "random-youtube":
        youtube_workout = YoutubeWorkout(workout_type, 1)
        return youtube_workout.get_random_workout(workout_type, 1)
