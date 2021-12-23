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

    items = response["items"]
    randomise_results = random.sample(items, number_of_videos)

    urls = []

    if number_of_videos == 3:
        for item in randomise_results:
            url = ("https://www.youtube.com/watch?v=" + item["id"]["videoId"]),
            urls.append(url)

    else:
        for item in randomise_results:
            url = ("https://www.youtube.com/watch?v=" + item["id"]["videoId"])
            urls.append(url)

    url_to_db(urls)

    return render_template('results.html', len=len(randomise_results), videos=randomise_results)


def url_to_db(urls):
    if request.method == 'POST':
        mysql = MySQL()
        conn = mysql.connection.cursor()
        conn.execute('''CREATE TABLE IF NOT EXISTS youtube_results (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        video_1 VARCHAR(500) NOT NULL, video_2 VARCHAR(500), video_3 VARCHAR(500), userid INT(11) NOT NULL) ''')
        if len(urls) == 3:
            conn.execute('INSERT INTO youtube_results (video_1, video_2, video_3, userid) VALUES (%s, %s, %s, %s)',
                         (urls[0], urls[1], urls[2], session['id'],))
        else:
            conn.execute('INSERT INTO youtube_results (video_1, userid) VALUES (%s, %s)',
                         (urls[0], session['id'],))
        mysql.connection.commit()
        conn.close()
