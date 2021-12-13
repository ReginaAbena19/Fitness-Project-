from flask import Blueprint, render_template, request
import os
import googleapiclient.discovery
import random


views = Blueprint('views', __name__)

"""
Need to figure out how the different function is called based on the results of the quiz so I've commented out 
exercise DB function for now 
"""


# @views.route('/results')
# def exercise_db():
#     # Add logic connecting quiz results to search api url with search terms
#     url = "https://exercisedb.p.rapidapi.com/exercises/bodyPart/back"
#
#     headers = {
#         'x-rapidapi-host': "exercisedb.p.rapidapi.com",
#         'x-rapidapi-key': "6491b9bedamsh60d64359f44595dp19a013jsn596072484b13"
#     }
#
#     response = requests.request("GET", url, headers=headers)
#     item_list = response.json()
#     exercise_names_list = []
#     exercise_equipment_list = []
#     exercise_gif_list = []
#     randomise_results = random.sample(item_list, 5)
#
#     for result in randomise_results:
#         exercise_names_list.append(result["name"])
#         exercise_equipment_list.append(result["equipment"])
#         exercise_gif_list.append(result["gifUrl"])
#
#     print(exercise_names_list)
#     print(exercise_equipment_list)
#     print(exercise_gif_list)
#
#     return render_template('results_exerciseDB.html', len=len(randomise_results), name=exercise_names_list,
#                            equipment=exercise_equipment_list, gif=exercise_gif_list)
#
#
# if __name__ == "__main__":
#     main()

@views.route('/results', methods=['GET', 'POST'])
def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyB5YfBeSnx_VnIDCmfkJHp5lzci9wNe4-E"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)
    requests = youtube.search().list(
        part="snippet",
        maxResults=100,
        q="leg strength workout",
    )
    response = requests.execute()

    items = response["items"]
    randomise_results = random.sample(items, 3)

    titles = []

    videos = []

    for item in randomise_results:
        videos.append(item['id']['videoId'])
        titles.append(item['snippet']['title'])

    print(videos)
    print(titles)

    return render_template('results.html', len=len(videos), videos=videos, titles=titles)


if __name__ == "__main__":
    main()
