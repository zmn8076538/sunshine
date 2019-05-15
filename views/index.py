from views import app
from flask import render_template,jsonify,redirect,url_for
from flask import request
from services.login_service import LoginService
from services.regist_service import RegistService

class IndexControll:

    login_service = LoginService()
    regist_service = RegistService()

    @app.route('/index')
    def index(self):
        return render_template('index.html')

    @app.route('/regist_index',methods=['GET'])
    def regist_index(self):
        return render_template('regist.html')

    @app.route('/login',methods=['POST'])
    def login(self):
        username = request.form['username']
        password = request.form['password']
        if self.login_service.login_by_username_password(username,password):
            return jsonify({'message':'success'})
        else:
            return jsonify({'message':'用户或密码错误'})

    @app.route('/regist',methods=['POST'])
    def regist(self):
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        result = self.regist_service.regist_by_upr(username, password, repassword)
        if result['flag'] == 0:
            return jsonify({'message':'用户名已存在'})
        if result['flag'] == 1:
            return jsonify({'message':'两次输入密码不一致'})
        if result['flag'] == 'success':
            return jsonify({'message':'注册成功,请登陆'})

    @app.route('/regist_login')
    def regist_login(self):
        return render_template('index.html')

    @app.route('/home',methods=['GET'])
    def home(self):
        return render_template('home.html')

    @app.route('/addCustomer',methods=['POST'])
    def add_customer(self):
        name = request.form['name']
        gender = request.form['gender']
        nidcard = request.form['idcard']
        bankcard = request.form['bankcard']
        safecard = request.form['safecard']
        phone = request.form['phone']
        naproduct = request.form['product']
        payment = request.form['payment']
        paymentyear = request.form['paymentyear']
        safeguard = request.form['safeguard']
        detail = request.form['detail']



