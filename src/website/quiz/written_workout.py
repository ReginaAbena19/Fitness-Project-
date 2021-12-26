import requests
from flask import render_template, request, Blueprint
import random
import pandas as pd

views = Blueprint('views', __name__)

"""
This is the class that is responsible for the Exercise DB API. It connects and sends API requests to the API 
based on the user's input, returns the response, and randomises the results to be displayed on the results page. 
"""


class WrittenWorkout:
    """
    This function creates the URL for the API request based on the user's selected
    body part and return the URL ready for the request.
    """
    def generate_url_for_api(self, selected_bodypart):
        url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/" + selected_bodypart
        return url

    """
     This function connects to the Exercise DB API.
     """
    def connect_to_exercisedb_api(self):
        payload = {}
        headers = {
            'x-rapidapi-host': "exercisedb.p.rapidapi.com",
            'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
        }
        return headers, payload

    """
    This function executes the request to the API.
    """
    def make_request_to_api(self, url, headers, payload):
        response = requests.request(
            "GET",
            url,
            headers=headers,
            data=payload
        )
        return response

    """
    This function randomises the results from the API response.
    """
    def randomise_api_result(self, response):
        item_list = response.json()
        randomise_results = random.sample(list(item_list), 5)
        return randomise_results

    """
    This function appends the results to lists of exercise names, equipment
    needed and GIF urls ready to be displayed in results page.
    """
    def append_results_to_lists(self, randomise_results):
        names_list = []
        equipment_list = []
        gif_list = []

        for result in randomise_results:
            names_list.append(result["name"])
            equipment_list.append(result["equipment"])
            gif_list.append(result["gifUrl"])

        return names_list, equipment_list, gif_list

    """
    This function creates a CSV of the written workout results. This is a workaround 
    storing the results in the database as MySQL can't take lists or JSON objects.
    """
    def create_workout_csv(self, randomise_results):
        df = pd.DataFrame(randomise_results)
        df.to_csv('workouts.csv', columns=[
            'bodyPart', 'equipment', 'gifUrl', 'id', 'name', 'target'
        ])

    """
    This function executes the above and renders the HTML template with 
    the results.
    """
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
