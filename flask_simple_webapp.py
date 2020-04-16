from flask import Flask, session
from checker import check_logged_in
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
import logging

sentry_sdk.init(
    dsn="https://bd717991e1bc4bafa2813e75a86f6611@o378968.ingest.sentry.io/5203137",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello from simple webapp.'


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1.'


@app.route('/erro')
def erro() -> int:
    try:
        return str(1/0)
    except:
        logging.exception('Erro')
        return str(0)


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3.'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'

"""
@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'
"""

app.secret_key = 'ADeathYouWillNeverEscape'
if __name__ == '__main__':
    app.run(debug=True, port='5521')