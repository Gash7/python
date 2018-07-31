from flask import*

application = Flask(__name__)


@application.route('/home')
def my_app():
    return 'Hi welcome to websesite.This is Interseting'


@application.route('/')
def My_login():
    return render_template('My_login.html')


if __name__ == '__main__':
    application.run(debug=True,port=8080)

