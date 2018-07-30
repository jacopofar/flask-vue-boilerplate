"""Vue Flask boilerplate backend entry point."""
import datetime
import logging

from flask import Flask, jsonify

app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s%(levelname)s %(message)s',
)


@app.route("/hello")
def hello():
    """Hello world‽."""
    return 'Hello world!'


@app.route("/current_time")
def current_time():
    """Give current ISO time."""
    return jsonify({'current_time':
                    datetime.datetime.utcnow().replace(
                        tzinfo=datetime.timezone.utc).isoformat()})
