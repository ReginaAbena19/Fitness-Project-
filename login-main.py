from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap

app = Flask (__name__)

Bootstrap(app)

@app.route('/login')
def index():
    return redirect(url_for('new_user'))
#redirected to homepage if login,username +password are correct-authenticated by db
#else directed to page showing e.g. "incorrect login" then they can signup
@app.route('/signup')
def new_user():
    return render_template ("sign up.html")

@app.route('/home')
def home():
    return render_template("home.html")
#appears if login is successful
@app.route('/logout')
def profile():
    return render_template("logout.html")

if __name__ =='__main__':
    app.run(debug=True)

