import requests
from flask import Blueprint
import random

views = Blueprint('views', __name__)


@views.route('/results/<workout_type>')
def get_written_workout(workout_type):
    url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{workout_type}" # Need to check if this works and
    # pulls parameters from the quiz in the same way as it does for the Youtube API (the search only works by body
    # part so should be "/bodyPart/back"

    headers = {
        'x-rapidapi-host': "exercisedb.p.rapidapi.com",
        'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
    }

    response = requests.request("GET", url, headers=headers)
    item_list = response.json()
    exercise_names_list = []
    exercise_equipment_list = []
    exercise_gif_list = []
    randomise_results = random.sample(item_list, 5)

    for result in randomise_results:
        exercise_names_list.append(result["name"])
        exercise_equipment_list.append(result["equipment"])
        exercise_gif_list.append(result["gifUrl"])

    print(exercise_names_list)
    print(exercise_equipment_list)
    print(exercise_gif_list)

    return get_written_workout()
