#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template


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
    number if int
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    number inside HTML
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
    number odd/even
    """
    if n % 2 == 0:
        oddeven_check = 'even'
    else:
        oddeven_check = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           oddeven_check=oddeven_check)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
