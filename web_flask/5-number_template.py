#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ route method displays text """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello2():
    """ display text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def displayparam(text):
    """ print out url param """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def displaydefaultparam(text="is cool"):
    """ print out url param """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ prints n if it is int """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ returns simple html page """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
