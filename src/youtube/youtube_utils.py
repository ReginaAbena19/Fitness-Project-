import os
import googleapiclient.discovery
import random

def get_workout_results_from_youtube(workout_type):
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
    randomise_results = random.sample(items, 3)

    return randomise_results

