from flask_mysqldb import MySQL

from src.main import app


def create_db():
    mysql = MySQL()
    conn = mysql.connect.cursor
    conn.execute('''CREATE DATABASE IF NOT EXISTS fitly''')
    mysql.connection.commit()
    conn.close()



