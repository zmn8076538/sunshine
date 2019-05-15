from cfg import cursor

class LoginDao:
    def login_get_password_by_username(self,username):
        sql = "select user_password from users where user_name = '{user_name}'"\
            .format(user_name=username)
        cursor.execute(sql)
        password = cursor.fetchone()[0]
        return password




