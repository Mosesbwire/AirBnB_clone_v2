#!/usr/bin/python3
""" Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ route method displays text """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello2():
    """ display text"""
    return "HBNB"


@app.route("/c/<text>", strict_slases=False)
def displayparam(text):
    """ print out url param """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
