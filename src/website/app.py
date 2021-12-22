from flask import Flask, render_template, request, redirect, session, flash, url_for
from functools import wraps
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'AbenaBenyiwa19'
app.config['MYSQL_DB'] = 'fitly'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# Login
@app.route('/')
@app.route('/login', methods=['POST', 'GET'])
def login():
    status = True
    if request.method == 'POST':
        email = request.form["email"]
        pwd = request.form["password"]
        cur = mysql.connection.cursor()
        cur.execute("select * from login where email=%s and Password1=%s", (email, pwd))
        data = cur.fetchone()
        if data:
            session['logged_in'] = True
            session['username'] = data["email"]
            flash('Login Successfully', 'success')
            return redirect('profile')
        else:
            flash('Invalid Login. Try Again', 'danger')
    return render_template("login.html")


# check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('login'))

    return wrap


# Registration
@app.route('/signup', methods=['POST', 'GET'])
def reg():
    status = False
    if request.method == 'POST':
        name = request.form["firstName"]
        email = request.form["email"]
        pwd1 = request.form["password1"]
        pwd2 = request.form["password2"]
        cur = mysql.connection.cursor()
        cur.execute("insert into login(firstname,email,Password1,password2) values(%s,%s,%s,%s)", (name, email,pwd1,pwd2,))
        mysql.connection.commit()
        cur.close()
        flash('Registration Successfully. Login Here...', 'success')
        return redirect('profile')
    return render_template("sign_up.html", status=status)


# Home page
@app.route("/home")
@is_logged_in
def home():
    return render_template('home.html')

# # profile/dashboard
@app.route("/profile")
def user():
    return render_template('profile.html')

# logout
@app.route("/logout")
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)
