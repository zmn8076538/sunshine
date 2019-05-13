from cfg import cursor

def is_exist_username(username):
    sql = "select * from users where user_name = '{user_name}'".format(user_name=username)
    cursor.execute(sql)
    return cursor.rowcount == 1

def regist_in_db(username,password):
    sql = "insert into users(user_name,user_password) values('{username}','{password}')"\
        .format(username=username,password=password)
    return cursor.execute(sql) == 1







