from cfg import cursor

def is_exist_username(username):
    sql = "select * from user where user_name = '{user_name}'".format(user_name=username)
    cursor.execute(sql)
    if cursor.rowcount == 1:
        return False
    else:
        return True

def regist_in_db(username,password):
    if is_exist_username(username):
        sql = "insert into user(user_name,user_password) values('{username}','{password}')"\
            .format(username=username,password=password)
        cursor.execute(sql)
        if cursor.rowcount == 1:
            return True
    else:
        raise Exception('用户名已存在')




