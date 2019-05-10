from views import app
from flask import render_template
from flask import request
from services.login_service import login_by_username_password
from services.regist_service import regist_by_upr

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

@app.route('/regist_index',methods=['GET'])
def regist_index():
    return render_template('regist.html')

@app.route('/regist',methods=['POST'])
def regist():
    username = request.form['username']
    password = request.form['password']
    repassword = request.form['repassword']
    if regist_by_upr(username,password,repassword):
        return render_template('index.html')
    else:
        return render_template('regist.html')

