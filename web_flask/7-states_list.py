#!/usr/bin/python3
""" Handles /states list route """
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def exeption(e):
    """ Teardown session """
    storage.close()


@app.route('/states_list')
def statesList():
    """ Handle route """
    state = storage.all("State")
    return render_template('7-states_list.html', state=state)


if __name__ == "__main__":
    app.run()
