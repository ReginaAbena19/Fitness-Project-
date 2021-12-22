import requests
from flask import render_template, request, Blueprint
import random
import pandas as pd
from flask_mysqldb import MySQL


def get_workout_history(user_id):
    mysql = MySQL()
    user = user_id
    conn = mysql.connection.cursor()
    results = conn.execute('SELECT * FROM youtube_results WHERE userid = %s', (user,))
    print(results)
    mysql.connection.commit()
    conn.close()
