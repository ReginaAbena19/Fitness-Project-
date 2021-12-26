import os
import googleapiclient.discovery
import random
from flask import render_template, request, session
from src.website.db import youtube_db_connection

"""
This is the class that is responsible for YouTube. It connects and sends API requests to the YouTube API, 
returns the results, randomises the results and inserts the results into the database. 
"""


class YoutubeWorkout:
    """
    The class constructor that will initialize all the key variables for the YoutubeWorkout class
    """

    def __init__(self, workout_type, number_of_videos):
        self.workout_type = workout_type
        self.number_of_videos = number_of_videos

    """
    This function connects to the YouTube Data API.
    """

    def connect_to_api(self):
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyB5YfBeSnx_VnIDCmfkJHp5lzci9wNe4-E"
        return api_service_name, api_version, DEVELOPER_KEY

    """
    This function connects to the YouTube Data API.
    """

    def get_youtube_api_result(self, api_service_name, api_version, developer_key):
        youtube = googleapiclient.discovery.build(
            api_service_name,
            api_version,
            developerKey=developer_key
        )

        requests = youtube.search().list(
            part="snippet",
            maxResults=100,
            q=self.workout_type,
        )
        response = requests.execute()
        return response

    """
    This function will take the API response randomise the results.
    """

    def randomise_results(self, response):
        items = response["items"]
        randomise_results = random.sample(items, self.number_of_videos)
        return randomise_results

    """
    This function will create the embeddable URLs to be stored in the database 
    as the user's workout history.
    """

    def create_urls_list_in_db(self, randomise_results):
        urls = []
        if self.number_of_videos == 3:
            for item in randomise_results:
                url = ("https://www.youtube.com/embed/" + item["id"]["videoId"]),
                urls.append(url)
        else:
            for item in randomise_results:
                url = ("https://www.youtube.com/embed/" + item["id"]["videoId"])
                urls.append(url)
        self.url_to_db(urls)

    """
    This function gets the final urls from the above functions and renders the results page. 
    """
    def get_workout_results_from_youtube(self, workout_type, number_of_videos):
        api_connection = self.connect_to_api()

        api_service_name = api_connection[0]
        api_service_version = api_connection[1]
        developer_key = api_connection[2]

        youtube_api_result = self.get_youtube_api_result(api_service_name, api_service_version, developer_key)
        randomised_results = self.randomise_results(youtube_api_result)

        self.create_urls_list_in_db(randomised_results)

        return render_template('results.html', len=len(randomised_results), videos=randomised_results)

    """
    This function returns a single random workout video without any parameters (no body part or location). 
    """
    def random_video_api(self, api_service_name, api_version, developer_key):
        youtube = googleapiclient.discovery.build(
            api_service_name,
            api_version,
            developerKey=developer_key
        )
        requests = youtube.search().list(
            part="snippet",
            maxResults=100,
            q="workout"
        )
        response_2 = requests.execute()
        return response_2

    """
    This function randomises the API response for the random workout.
    """
    def random_workout_result(self, response_2):
        items = response_2["items"]
        random_video = random.sample(items, 1)
        return random_video

    """
    This function gets the final url from the above functions and renders the results page with the single random
    workout video. 
    """
    def get_random_workout(self, workout_type, number_of_videos):
        api_connection = self.connect_to_api()

        api_service_name = api_connection[0]
        api_service_version = api_connection[1]
        developer_key = api_connection[2]

        random_api_result = self.random_video_api(api_service_name, api_service_version, developer_key)
        random_workout = self.random_workout_result(random_api_result)

        self.random_video_url_in_db(random_workout)

        return render_template('results.html', len=len(random_workout), videos=random_workout)

    """
    This function will create the embeddable URL for the random workout to be stored in the database 
    as the user's workout history.
    """
    def random_video_url_in_db(self, random_workout):
        urls = []
        for item in random_workout:
            url = ("https://www.youtube.com/embed/" + item["id"]["videoId"])
            urls.append(url)
        self.url_to_db(urls)

    """
    This function will insert the URL(s) from the request into the database.
    """
    def url_to_db(self, urls):
        if request.method == 'POST':
            session_id = session['id']

            db = youtube_db_connection.youtubeDbConnection
            connection = db.connect_to_database()

            db.create_youtube_workout_table(connection)

            if len(urls) == 3:
                db.add_personalised_workout_to_db(connection, urls, session_id)
            else:
                db.add_random_workout_to_do(connection, urls, session_id)

            db.commit_to_database()
            db.close_database_connection(connection)
