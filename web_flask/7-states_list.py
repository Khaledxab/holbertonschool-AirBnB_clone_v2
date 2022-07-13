#!/usr/bin/python3
"""list of states"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """storage close"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def statesList():
    """statelist method"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run()
