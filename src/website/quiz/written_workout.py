import requests
from flask import render_template, request, Blueprint
import random
import pandas as pd

views = Blueprint('views', __name__)


def get_written_workout():
    selected_bodypart = request.form['muscle-group']
    url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/" + selected_bodypart

    payload = {
    }

    headers = {
        'x-rapidapi-host': "exercisedb.p.rapidapi.com",
        'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    item_list = response.json()
    names_list = []
    equipment_list = []
    gif_list = []
    randomise_results = random.sample(list(item_list), 5)

    print(randomise_results)

    df = pd.DataFrame(randomise_results)
    df.to_csv('workouts.csv', columns=[
        'bodyPart', 'equipment', 'gifUrl', 'id', 'name', 'target'
    ])

    for result in randomise_results:
        names_list.append(result["name"])
        equipment_list.append(result["equipment"])
        gif_list.append(result["gifUrl"])

    print(names_list)
    print(equipment_list)
    print(gif_list)

    return render_template("results_written.html", len=len(randomise_results), names=names_list,
                           equipments=equipment_list, gifs=gif_list, selected_bodypart=selected_bodypart, url=url)
