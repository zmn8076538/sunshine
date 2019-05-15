from daos.login_dao import LoginDao

class LoginService:

    login_dao = LoginDao()

    #通过用户名获取password
    def login_by_username_password(self,username,password):
        password_in_db = self.login_dao.login_get_password_by_username(username)
        return password == password_in_db

    #通过用户名获取user_id字段
    def login_get_userid(self,username):
        return self.login_dao.login_get_userid_by_username(username)
