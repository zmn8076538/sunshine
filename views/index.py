from views import app
from flask import render_template
from flask import request

@app.route('/index')
def index():

    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return render_template('home.html')

