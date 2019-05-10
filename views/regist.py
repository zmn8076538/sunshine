from views import app
from flask import render_template

@app.route('/regist')
def user_regist():

    return render_template('regist.html')

