from flask import Flask, render_template,,redirect,url_for,request,session
from flask_mysql_connector import MySQL
#or from flask_mysqldb import MySQL
import MySQLdb


app = Flask (__name__)
app.secret_key = "nanotechdegree"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"]= "AbenaBenyiwa19"
app.config["MYSQL_DATABASE"]= "login"

db = MySQL(app)

@app.route('/',methods= ['GET','POST'])
def index():
    if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        cursor = db.connection.cursor(MySQLdb.cursors.dictCursor)
        cursor.execute("SELECT * FROM login_info WHERE username=%s AND user_password=%s",(username,password))
        info = cursor.fetchone()
        if info is not None:
         if info['username'] == username and info['user_password'] == password:
             session['loginsuccess'] = True
            return"login succesful"#/ return redirect(url_for("home.html))
        else:
            return "login unsuccessful, please register"
        return render_template("login.html")#/redirect(url_for('index'))

#might need to edit signup(to match db values) html for this to work
        #@app.route('/new')
        #def new_user():
        if request.method == "POST":
            if "one" in request.form and "two" in request.form and "three" in request.form and "four" in request.form
                email = request.form['one']
                firstname = request.form['two']
                password = request.form['three']
                password2 = request.form['four']
                cur= db.connection.cursor(MySQLdb.cursors.DictCursor)
        #return render_template("signup.html)

        #@app.route('/new/profile')
        # def profile():
        # if session['loginsuccess]==True:
        #return render_template(home.html)

        if __name__ == '__main__':
            app.run(debug=True)