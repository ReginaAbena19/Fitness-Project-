import os
import googleapiclient.discovery
import random

from flask import render_template


def get_workout_results_from_youtube(workout_type, number_of_videos):
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyB5YfBeSnx_VnIDCmfkJHp5lzci9wNe4-E"
    youtube = googleapiclient.discovery.build(
        api_service_name,
        api_version,
        developerKey=DEVELOPER_KEY
    )
    requests = youtube.search().list(
        part="snippet",
        maxResults=100,
        q=workout_type
    )
    response = requests.execute()

    items = response["items"]
    randomise_results = random.sample(items, number_of_videos)

    return render_template('results.html', len=len(randomise_results), videos=randomise_results)
