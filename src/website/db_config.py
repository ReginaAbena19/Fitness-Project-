from flask_mysqldb import MySQL
from src.main import app

"""
This function attempted to create the fitly database but wasn't successful
so we've adapted the prerequisites to ask users to create the database before
running the app.
"""
def create_db():
    mysql = MySQL()
    conn = mysql.connect.cursor
    conn.execute('''CREATE DATABASE IF NOT EXISTS fitly''')
    mysql.connection.commit()
    conn.close()



