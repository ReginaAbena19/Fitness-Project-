from flask_mysqldb import MySQL

"""
This class creates the connection between the Flask app and database to store user 
account information. 
"""


class userAccountDbConnection:
    def __init__(self):
        self.mysql = MySQL()

    def connect_to_database():
        mysql = MySQL()
        conn = mysql.connection.cursor()
        return conn

    def close_database_connection(conn):
        return conn.close()

    def create_user_table(conn):
        conn.execute(''' CREATE TABLE IF NOT EXISTS users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                     name VARCHAR(100) NOT NULL,
                     email VARCHAR(100) NOT NULL,
                     password VARCHAR(1000) NOT NULL) ''')
        return conn

    def check_if_user_exists_in_db(conn, email):
        conn.execute('SELECT * FROM users WHERE email = % s ', (email,))
        user = conn.fetchone()
        return user

    def insert_new_user(conn, name, email, password):
        conn.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password,))

    def commit_to_database():
        mysql = MySQL()
        mysql.connection.commit()
        print("DONE")
