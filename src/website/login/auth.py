from flask import Flask, render_template, redirect,url_for

app = Flask (__name__, template_folder ='templates')

@app.route('/home')
def index():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/signup')
def new_user():
    return render_template("sign_up.html")

#if the login is successful
@app.route('/profile')
def user_profile():
    return render_template("profile.html")
#e.g.
@app.route('/login')
def login():
    return redirect(url_for('user_profile'))

@app.route('/logout')
def logout():
    return render_template("logout.html")

if __name__ =='__main__':
    app.run(debug=True)
