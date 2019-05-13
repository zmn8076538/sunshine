from daos.login_dao import login_get_password_by_username

def login_by_username_password(username,password):
    password_in_db = login_get_password_by_username(username)
    return password == password_in_db
