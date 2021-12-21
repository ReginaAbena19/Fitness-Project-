from flask import Flask, render_template,redirect,url_for,request,session
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
        if 'email' in request.form and 'password' in request.form:
         email = request.form['email']
         password = request.form['password']

        cursor = db.connection.cursor(MySQLdb.cursors.dictCursor)
        cursor.execute("SELECT * FROM login_info WHERE user_email=%s AND user_password=%s",(email,password))
        info = cursor.fetchone()
        if info is not None:
         if info['user_email'] == email and info['user_password'] == password:
             session['loginsuccess'] = True
             return redirect(url_for("profile"))
        else:
             return redirect(url_for("login"))

@app.route('/new',methods =['GET','POST'])
def new_user():

     if request.method == "POST":
            if "email" in request.form and "firstname" in request.form and "password" in request.form and "password2" in request.form:
                email = request.form['email']
                firstname = request.form['firstname']
                password = request.form['password']
                password2 = request.form['password2']
                cur= db.connection.cursor(MySQLdb.cursors.DictCursor)


            cur.execute("INSERT INTO fitly.login_info(user_email,user_name,user_password,user_password) VALUES" ("%s,%s,%s,%s)",(email,firstname,password,password2))
            db.connection.commit()
                return redirect(url_for("profile"))
            return render_template("sign_up.html")

@app.route('/new/profile')
def profile():
   if session ['lognsuccess'] == True:
    return render_template ("profile.html")

@app.route ('/new/logout')
def logout():
    session.pop('loginsuccess', None)
    return redirect(url_for("login"))
#need to add new logout part to profile html