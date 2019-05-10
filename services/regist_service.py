from daos.regist_dao import regist_in_db,is_exist_username

def regist_by_upr(username,password,repassword):
    if password == repassword:
        if is_exist_username(username):
            raise Exception('用户名已存在')
        else:
            return regist_in_db(username,password)
    else:
        raise Exception('两次输入密码不一致')
