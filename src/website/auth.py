import re
from flask import Blueprint, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
from src.website.profile.retrieve_workout_history import get_workout_history

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        mysql = MySQL()
        conn = mysql.connection.cursor()
        conn.execute('SELECT * FROM users WHERE email = % s AND password = % s ', (email, password,))
        user = conn.fetchone()
        print(user)
        if user:
            session['loggedin'] = True
            session['id'] = user[0]
            session['email'] = user[1]
            print("Logged in successfully")
            return redirect('/')
        else:
            print("Incorrect username or password")
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)

    return redirect('/login')
    # could we have this redirect to the logout page?
    # return render_template("logout.html", boolean=True)

@auth.route('/profile')
def profile():
    user_id = session.get('id')
    get_workout_history(user_id)
    return render_template("profile.html")



@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        mysql = MySQL()
        conn = mysql.connection.cursor()
        conn.execute(''' CREATE TABLE IF NOT EXISTS users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                     email VARCHAR(100) NOT NULL,
                     password VARCHAR(20) NOT NULL) ''')
        conn.execute('SELECT * FROM users WHERE email = % s ', (email,))
        user = conn.fetchone()
        if user:
            print('Account already exists')
        elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            print('Invalid email address')
        elif not email or not password:
            print('Please fill out the form')
        else:
            conn.execute('INSERT INTO users (email, password) VALUES (%s, %s)', (email, password,))
            mysql.connection.commit()
            return redirect('/login')
        conn.close()
        print("DONE")

    return render_template("sign_up.html")
