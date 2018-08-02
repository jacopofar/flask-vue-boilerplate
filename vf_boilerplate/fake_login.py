"""Module to perform a fake login and instantiate the user session.

Used for development ONLY.
"""
import logging
import time

from flask import Flask, jsonify, make_response, session

app = Flask(__name__)
app.secret_key = 'dev'

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s%(levelname)s %(message)s',
)


@app.route("/")
def index():
    """Log in an user, used only in dev mode."""
    session['mail'] = 'test.user@example.com'
    session['name'] = 'Luther Blissett'
    # iat is in the session but never used, here is for debugging
    # for the "real world" you probably want to use PyJWT
    session['iat'] = int(time.time())
    return "You are now logged in for development!"


@app.route("/whoami")
def whoami():
    """Retrieve the user identity from the session."""
    if 'mail' not in session:
        logger.info('Session not present, the user is not logged in')
        return make_response(jsonify(error='not logged in'), 400)
    logger.info('The user has a valid session')
    return jsonify(
        mail=session['mail'],
        name=session['name'])
