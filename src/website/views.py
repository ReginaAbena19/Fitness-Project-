from flask import Blueprint, render_template, request, session
from src.website.quiz.written_workout import get_written_workout
from werkzeug.utils import redirect

from src.website.youtube.youtube_utils import get_workout_results_from_youtube

views = Blueprint('views', __name__)


@views.route('/', methods=["POST", "GET"])
def home():
    if session:
        return render_template("home.html")
    else:
        return redirect('/login')


@views.route('/results/', methods=["POST", "GET"])
def results():
    workout_type = request.form['workout-location'] + "+" + request.form['muscle-group'] + "+" + "workout"
    if request.form['submit-button'] == "written":
        return get_written_workout()
    elif request.form['submit-button'] == "personalised-youtube":
        return get_workout_results_from_youtube(workout_type, 3)
    elif request.form['submit-button'] == "random-youtube":
        return get_workout_results_from_youtube(workout_type, 1)
