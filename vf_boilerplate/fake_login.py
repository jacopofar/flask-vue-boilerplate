"""Module to perform a fake login and instantiate the user session.

Used for development ONLY.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    """Log in an user, used only in dev mode."""
    return "You are logged in for development!"
