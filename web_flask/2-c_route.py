#!/usr/bin/python3
"""
Starts a Flask web application three routes + text
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Starting a Flask web app
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
    Displays HBNB
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    Displays C + <text>
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
