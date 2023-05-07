from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>This is my Home Page</h1>'


@app.route('/signin_from', methods=['GET'])
def signin_from():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'test' and request.form['password'] == 'test':
        return '<h1>Welcome, test!</h1>'
    return '<h1>Sorry, bad username</h1>'


if __name__ == 'main':
    app.run()

