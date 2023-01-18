#!/usr/bin/python3
"""
    Starts a Flask web application.
        The application listens on 0.0.0.0, port 5000.
        Routes:
            /: Displays 'Hello HBNB!'
            /hbnb: Displays 'HBNB'
            /c/<text>: display “C ” followed by the value of the text variable
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


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """ Displays custom input text supplied """
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
