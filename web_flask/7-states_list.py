#!/usr/bin/python3
"""
    Python flask script to print a list of states
"""

from flask import Flask, render_template, g
from models import storage
app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def state_list(states):
    states = storage.all()
    return render_template(states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
