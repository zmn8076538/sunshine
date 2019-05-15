from daos.login_dao import LoginDao

class LoginService:

    login_dao = LoginDao()

    def login_by_username_password(self,username,password):
        password_in_db = self.login_dao.login_get_password_by_username(username)
        return password == password_in_db
