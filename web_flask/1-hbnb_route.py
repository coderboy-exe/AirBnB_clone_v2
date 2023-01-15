#!/usr/bin/python3
"""
    Starts a Flask web application.
        The application listens on 0.0.0.0, port 5000.
        Routes:
            /: Displays 'Hello HBNB!'
            /hbnb: Displays 'HBNB'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays the text """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Dispalays text """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
