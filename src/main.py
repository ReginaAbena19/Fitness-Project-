from flask_mysqldb import MySQL
import os
from src.website import create_app

"""
This file creates the flask app and configures the database. The user must add their root password and 
the already-created database for the app to run successfully.
"""
app = create_app()
app.secret_key = os.urandom(12)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '<INSERT PASSWORD>'  # insert your root password here
app.config['MYSQL_DB'] = '<INSERT DB NAME>'  # create database for app before running, e.g. fitly_results

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)
