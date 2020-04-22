#!/usr/bin/python3
"""starts a Flask web app two routes"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """start a flask web app"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Display HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
