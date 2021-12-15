from flask import Blueprint, render_template, request
import random
from googleapiclient.discovery import build

views = Blueprint('views', __name__)

"""The way the search API key works, it retrieves the first 100 videos related to the keyword 'workout'.
added a filter 'date', which sorts the videos in reverse chronological order of the date of creation (from newest to
oldest). This ensures the function will return new videos as they are uploaded."""

@views.route('/results', methods=['GET', 'POST'])
def get_random_workout():
    API_key = "AIzaSyBXFdFDEHW8j4d82FOY-mVLLLSwodhYlF0"
    youtube = build("youtube", "v3", developerKey=API_key)
    request = youtube.search().list(
        part="snippet",
        maxResults=100,
        q="workout",
        order="date"
    )
    response = request.execute()
    items = response["items"]

    random_video = random.choice(items)
    random_video_id = random_video["id"]["videoId"]
    random_video_title = randon_video["snippet"]["title"]
    
    print(random_video_id)
    print(random_video_title)

    return render_template('results.html', len=len(random_video_id), videos=random_video_id, title=random_video_title)



