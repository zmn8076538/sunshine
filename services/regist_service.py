from daos.regist_dao import regist_in_db

def regist_by_upr(username,password,repassword):
    if password == repassword:
        if regist_in_db(username,password):
            print('注册成功')
            return True
        else:
            raise Exception('注册失败')
    else:
        raise Exception('两次输入密码不一致')
