from flask import Flask, render_template, redirect,url_for

app = Flask (__name__, template_folder ='templates')


@app.route('/')
def index():
    return render_template("base.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/signup')
def new_user():
    return render_template("signup.html")

@app.route('/logout')
def profile():
    return render_template("logout.html")

if __name__ =='__main__':
    app.run(debug=True)
