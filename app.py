# from flask import Flask, url_for

# FlaskApp = Flask(__name__)

# @FlaskApp.route("/")
# def HelloFlask():
#     return '<h1>Hello Flask!!</h1>'

# @FlaskApp.route("/login/<ID>")
# def login_id(ID):
#     return '<h1>login ID: %s</h1>' % ID

# @FlaskApp.route("/pass/<int:PASS>")
# def pass_num(PASS):
#     return '<h1>Password: %s</h1>' % PASS

# if __name__ == '__main__':
#     FlaskApp.debug = True
#     with FlaskApp.test_request_context():
#         print(url_for('login_id', ID = 'Klasse'))
#         print(url_for('pass_num', PASS = 1234))

# from flask import Flask, render_template

# FlaskApp = Flask(__name__)

# @FlaskApp.route("/")
# def Hello():
#     return '<h1>Klasse</h1>'

# @FlaskApp.route("/userinfo1/<username>")
# def user(username):
#     return render_template("UserInfo1.html", name=username)

# @FlaskApp.route("/userinfo2/<username>/<location>/<age_num>")
# def user2(username, location, age_num):
#     return render_template("/UserInfo2.html", name=username, country=location, age=age_num)

# if __name__ == '__main__':
#     FlaskApp.run()