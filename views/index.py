from views import app
from flask import render_template
from flask import request
from services.login_service import login_by_username_password

@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if login_by_username_password(username,password):
        return render_template('home.html')
    else:
        return render_template('index.html')

