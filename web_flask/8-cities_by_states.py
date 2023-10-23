#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)
@app.route('/cities_by_states', strict_slashes=False)
def state_list():
    """
    list state
    """
    states = storage.all("State").values()
    cities = storage.all("City").values()
    return render_template("8-cities_by_states.html", states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(err):
    """
    teardown
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)