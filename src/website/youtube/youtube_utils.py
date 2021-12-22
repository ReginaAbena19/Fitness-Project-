import os
import googleapiclient.discovery
import random
from flask import render_template, request, session
from flask_mysqldb import MySQL


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
        q=workout_type,
    )
    response = requests.execute()

    urls = []

    items = response["items"]
    randomise_results = random.sample(items, number_of_videos)

    for item in randomise_results:
        url1 = ("https://www.youtube.com/watch?v=" + item["id"]["videoId"]),
        url2 = ("https://www.youtube.com/watch?v=" + item["id"]["videoId"]),
        url3 = ("https://www.youtube.com/watch?v=" + item["id"]["videoId"])

        urls.append(url1)
        urls.append(url2)
        urls.append(url3)

        url_to_db(url1, url2, url3)

    return render_template('results.html', len=len(randomise_results), videos=randomise_results)


def url_to_db(url1, url2, url3):
    if request.method == 'POST':
        mysql = MySQL()
        conn = mysql.connection.cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS youtube_results (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        video_1 VARCHAR(500) NOT NULL, video_2 VARCHAR(500) 
        NOT NULL, video_3 VARCHAR(500) NOT NULL, userid INT(11) NOT NULL) ''')
        conn.execute('INSERT INTO youtube_results (video_1, video_2, video_3, userid) VALUES (%s, %s, %s, %s)',
                     (url1, url2, url3, session['id'],))
        mysql.connection.commit()
        conn.close()
