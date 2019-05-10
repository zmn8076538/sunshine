from cfg import cursor

def login_get_password_by_username(username):
    sql = "select user_password from user where user_name = '{user_name}'"\
        .format(user_name=username)
    cursor.execute(sql)
    password = cursor.fetchone()[0]
    return password




