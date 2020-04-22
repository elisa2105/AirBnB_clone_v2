#!/usr/bin/python3
"""
Starts a Flask web application
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
    HBNB
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
    C + <text> variable
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """
    Python + <text>
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
