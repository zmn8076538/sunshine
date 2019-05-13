from daos.regist_dao import regist_in_db,is_exist_username

def regist_by_upr(username,password,repassword):
    if password == repassword:
        if is_exist_username(username):
            return {'flag': 0}
        elif regist_in_db(username, password):
            return {'flag': 'success'}
    else:
        return {'flag':1}


# #判断用户名、密码、确认密码是否为空
# def isNull(username,password,repassword):
#     if username == None or password == None or repassword == None:
#         return 0
