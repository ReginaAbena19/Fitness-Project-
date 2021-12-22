import re
from flask import Blueprint, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
from src.website.profile.retrieve_workout_history import get_workout_history
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        mysql = MySQL()
        conn = mysql.connection.cursor()
        conn.execute('SELECT * FROM users WHERE email = % s ', (email,))
        user = conn.fetchone()
        print(user)
        if user:
            if check_password_hash(user[2], password):
                session['loggedin'] = True
                session['id'] = user[0]
                session['email'] = user[1]
                print("Logged in successfully")
                return redirect('/')
            else:
                flash('Incorrect password', category='error')
        else:
            flash('Incorrect username', category='error')
    return render_template("login.html", boolean=True)


@auth.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)

    # return redirect('/login')
    # could we have this redirect to the logout page?
    return render_template("logout.html")


@auth.route('/profile')
def profile():
    user_id = session.get('id')
    get_workout_history(user_id)
    return render_template("profile.html")


@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'], method='sha256')
        mysql = MySQL()
        conn = mysql.connection.cursor()
        conn.execute(''' CREATE TABLE IF NOT EXISTS users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                     name VARCHAR(50) NOT NULL,
                     email VARCHAR(100) NOT NULL,
                     password VARCHAR(1000) NOT NULL) ''')
        conn.execute('SELECT * FROM users WHERE email = % s ', (email,))
        user = conn.fetchone()
        if user:
            print('Account already exists')
        elif not re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            print('Invalid email address')
        elif not email or not password:
            print('Please fill out the form')
        else:
            conn.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password,))
            mysql.connection.commit()
            return redirect('/login')
        conn.close()
        print("DONE")

    return render_template("sign_up.html")
