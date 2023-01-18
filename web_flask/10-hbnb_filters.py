#!/usr/bin/python3
""" State route """
from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def exeption(e):
    """ close session """
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """display html page with working city/state filters & amenities
       runs with web static css files
    """
    state_objs = [s for s in storage.all("State").values()]
    amenity_objs = [a for a in storage.all("Amenity").values()]
    return render_template('10-hbnb_filters.html',
                           state_objs=state_objs, amenity_objs=amenity_objs)

if __name__ == "__main__":
    app.run()
