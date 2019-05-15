from views import app
from flask import render_template,jsonify,redirect,url_for
from flask import request
from services.login_service import LoginService
from services.regist_service import RegistService
from services.add_customer_service import AddCustomerService


login_service = LoginService()
regist_service = RegistService()
add_customer_service = AddCustomerService()

userid = None


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/regist_index',methods=['GET'])
def regist_index():
    return render_template('regist.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if login_service.login_by_username_password(username,password):
        global userid
        userid = login_service.login_get_userid(username)
        return jsonify({'message':'success','userId':userid})
    else:
        return jsonify({'message':'用户或密码错误'})

@app.route('/regist',methods=['POST'])
def regist():
    username = request.form['username']
    password = request.form['password']
    repassword = request.form['repassword']
    result = regist_service.regist_by_upr(username, password, repassword)
    if result['flag'] == 0:
        return jsonify({'message':'用户名已存在'})
    if result['flag'] == 1:
        return jsonify({'message':'两次输入密码不一致'})
    if result['flag'] == 'success':
        return jsonify({'message':'注册成功,请登陆'})

@app.route('/regist_login')
def regist_login():
    return render_template('index.html')

@app.route('/home',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/addCustomer',methods=['POST'])
def add_customer():
    userId = request.form['userId']
    name = request.form['name']
    gender = request.form['gender']
    idcard = request.form['idcard']
    bankcard = request.form['bankcard']
    safecard = request.form['safecard']
    phone = request.form['phone']
    product = request.form['product']
    payment = request.form['payment']
    paymentyear = request.form['paymentyear']
    safeguard = request.form['safeguard']
    detail = request.form['detail']
    print(userId)
    if add_customer_service.add_customer(userId,name,gender,phone,product,payment,paymentyear,safeguard,detail,idcard,bankcard,safecard):
        return jsonify({'message':'添加成功'})
    return jsonify({'message':'添加失败'})




