import random
from googleapiclient.discovery import build

API_key = "AIzaSyBXFdFDEHW8j4d82FOY-mVLLLSwodhYlF0"
youtube = build("youtube", "v3", developerKey=API_key)

"""The way the search API key works, it retrieves the first 25 videos related to the keyword 'workout'.
added a filter 'date', which sorts the videos in reverse chronological order of the date of creation (from newest to
oldest). This ensures the function will return new videos as they are uploaded."""


def get_random_workout():
    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="workout",
        order="date"
    )
    response = request.execute()
    items = response["items"]

    random_video = random.choice(items)
    random_video_id = random_video["id"]["videoId"]
    random_video_link = f"https://www.youtube.com/watch?v={random_video_id}"

    return render_template('results.html', len=len(random_video_link), videos=random_video_link)



