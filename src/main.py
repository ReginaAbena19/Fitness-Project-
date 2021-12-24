from flask_mysqldb import MySQL
import os
from src.website import create_app

app = create_app()
app.secret_key = os.urandom(12)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '<INSERT PASSWORD HERE>' #insert your root password here
app.config['MYSQL_DB'] = '<INSERT DB HERE>'

mysql = MySQL(app)

if __name__ == '__main__':
    app.run(debug=True)
