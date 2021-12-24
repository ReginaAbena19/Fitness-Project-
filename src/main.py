from flask_mysqldb import MySQL
import os
from src.website import create_app

app = create_app()
app.secret_key = os.urandom(12)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AbenaBenyiwa19' #insert your root password here
app.config['MYSQL_DB'] = 'Fitly'

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)
