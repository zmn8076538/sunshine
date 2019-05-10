from views import app
from flask import render_template

@app.route('/login')
def user_login():

    return render_template('login.html')

