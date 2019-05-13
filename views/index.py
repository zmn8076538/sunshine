from views import app
from flask import render_template,jsonify
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
    result = regist_by_upr(username, password, repassword)
    if result['flag'] == 0:
        return jsonify({'message':'用户名已存在'})
    if result['flag'] == 1:
        return jsonify({'message':'两次输入密码不一致'})
    if result['flag'] == 'success':
        return jsonify({'message':'注册成功'})

@app.route('/regist_login')
def regist_login():
    return render_template('index.html')

