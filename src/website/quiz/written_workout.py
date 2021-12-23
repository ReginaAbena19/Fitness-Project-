import requests
from flask import render_template, request, Blueprint
import random
import pandas as pd

views = Blueprint('views', __name__)

class WrittenWorkout:
    def generate_url_for_api(self, selected_bodypart):
        url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/" + selected_bodypart
        return url

    def connect_to_exercisedb_api(self):
        payload = {}
        headers = {
            'x-rapidapi-host': "exercisedb.p.rapidapi.com",
            'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
        }
        return headers, payload

    def make_request_to_api(self, url, headers, payload):
        response = requests.request(
            "GET",
            url,
            headers=headers,
            data=payload
        )
        return response

    def randomise_api_result(self, response):
        item_list = response.json()
        randomise_results = random.sample(list(item_list), 5)
        return randomise_results

    def append_results_to_lists(self, randomise_results):
        names_list = []
        equipment_list = []
        gif_list = []

        for result in randomise_results:
            names_list.append(result["name"])
            equipment_list.append(result["equipment"])
            gif_list.append(result["gifUrl"])

        return names_list, equipment_list, gif_list

    def create_workout_csv(self, randomise_results):
        df = pd.DataFrame(randomise_results)
        df.to_csv('workouts.csv', columns=[
            'bodyPart', 'equipment', 'gifUrl', 'id', 'name', 'target'
        ])




    def get_written_workout(self):
        selected_bodypart = request.form['muscle-group']
        url = self.generate_url_for_api(selected_bodypart)

        api_connection = self.connect_to_exercisedb_api()

        api_response = self.make_request_to_api(
            url,
            api_connection[0],
            api_connection[1]
        )

        randomised_results = self.randomise_api_result(api_response)

        list_results = self.append_results_to_lists(randomised_results)
        self.create_workout_csv(randomised_results)


        return render_template(
            "results_written.html",
            len=len(randomised_results),
            names=list_results[0],
            equipments=list_results[1],
            gifs=list_results[2],
            selected_bodypart=selected_bodypart,
            url=url
        )
