#!/usr/bin/python3
"""Starts a Flask web app states and related cities
"""
from models import storage, State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """HTML states and related cities
    """
    return render_template("8-cities_by_states.html", it=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
