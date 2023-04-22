#!/usr/bin/python3
"""
    Python flask script to create routes
    to states
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=True)
def states():
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    pass