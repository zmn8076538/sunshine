from views import app
from flask import render_template,jsonify,redirect,url_for
from flask import request
from services.login_service import LoginService
from services.regist_service import RegistService
from services.add_customer_service import AddCustomerService
from services.get_customers_service import GetCustomersService
from services.delete_customer_service import DeleteCustomerService


login_service = LoginService()
regist_service = RegistService()
add_customer_service = AddCustomerService()
get_customers_service = GetCustomersService()
delete_customer_service = DeleteCustomerService()

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
    insurename = request.form['insurename']
    insuregender = request.form['insuregender']
    insureidcard = request.form['insureidcard']
    byinsurename = request.form['byinsurename']
    byinsuregender = request.form['byinsuregender']
    byidcard = request.form['byidcard']
    relationship = request.form['relationship']
    phone = request.form['phone']
    address = request.form['address']
    bankcard = request.form['bankcard']
    issuename = request.form['issuename']
    safecard = request.form['safecard']
    paymentperiod = request.form['paymentperiod']
    safeguardperiod = request.form['safeguardperiod']
    effectiveandexpirationdate = request.form['effectiveandexpirationdate']
    ordertime = request.form['ordertime']
    notdealreason = request.form['notdealreason']
    notorderreason = request.form['notorderreason']
    shareperson = request.form['shareperson']
    detail = request.form['detail']
    status = request.form['status']

    #客户状态
    if status == 'alreadyorder':
        status = 1
    elif status == 'impressive':
        status = 2
    elif status == 'delayordertime':
        status = 3
    elif status == 'visit':
        status = 4
    else:
        status = 5

    #投被保险人关系
    if relationship == 'self':
        relationship = 1
    elif relationship == 'marriage':
        relationship = 2
    elif relationship == 'fatherdaughter':
        relationship = 3
    elif relationship == 'fatherchild':
        relationship = 4
    elif relationship == 'motherdaughter':
        relationship = 5
    else:
        relationship = 6

    if add_customer_service.add_customer(userId,insurename,insuregender,insureidcard,byinsurename,byinsuregender,byidcard,relationship,phone,address,bankcard,issuename,safecard,paymentperiod,safeguardperiod,effectiveandexpirationdate,ordertime,notdealreason,notorderreason,shareperson,detail,status):
        return jsonify({'message':'添加成功'})
    return jsonify({'message':'添加失败'})

@app.route('/getCustomers_hasOrder',methods=['POST'])
def get_customers_not_contact():
    userId = request.form['userId']
    customers = get_customers_service.get_customers_has_order(userId)
    return jsonify(customers)

@app.route('/deleteCustomer',methods=['POST'])
def delete_customer():
    customer_id = request.form['customer_id']
    delete_customer_service.delete_customer(customer_id)
    return jsonify({"message":"success"})



