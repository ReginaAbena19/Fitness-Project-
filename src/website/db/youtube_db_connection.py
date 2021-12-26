from flask_mysqldb import MySQL

"""
This class creates the connection between the Flask app and database to store the YouTube results. 
"""


class youtubeDbConnection:

    def __init__(self):
        self.mysql = MySQL()

    def connect_to_database():
        mysql = MySQL()
        conn = mysql.connection.cursor()
        return conn

    def close_database_connection(conn):
        return conn.close()

    def create_youtube_workout_table(conn):
        conn.execute('''CREATE TABLE IF NOT EXISTS youtube_results (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        video_1 VARCHAR(500) NOT NULL, video_2 VARCHAR(500), video_3 VARCHAR(500), userid INT(11) NOT NULL) ''')
        print("created table")

    def add_personalised_workout_to_db(conn, urls, session_id):
        conn.execute('INSERT INTO youtube_results (video_1, video_2, video_3, userid) VALUES (%s, %s, %s, %s)',
                     (urls[0], urls[1], urls[2], session_id,))
        print("added 3 videos to db")

    def add_random_workout_to_do(conn, urls, session_id):
        conn.execute('INSERT INTO youtube_results (video_1, userid) VALUES (%s, %s)',
                     (urls[0], session_id,))
        print("added 1 video to db")

    def commit_to_database():
        mysql = MySQL()
        mysql.connection.commit()
        print("DONE")
