#!/usr/bin/python3
"""
Starts a Flask web application Four routes
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """
    Starting a Flask web app"""
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
    C + <text>
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """
    Python + <text>
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def numbers_only(n):
    """
    number n if int
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
