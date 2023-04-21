#!/uar/bin/python3
"""
    Python flask web app script to display
    the states and the cities
"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardowndb(self):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
