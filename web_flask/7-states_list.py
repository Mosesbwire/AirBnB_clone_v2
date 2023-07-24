#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
from models import *
from models import storage
import json

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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ returns html template """
    str_val = "even" if n % 2 == 0 else "odd"

    print(str_val)
    return render_template('6-number_odd_or_even.html', n=n, str_val=str_val)


@app.route("/states_list", strict_slashes=False)
def allStates():
    """ returns html with all the states from the db """
    obj = storage.all()
    states = []
    for name in obj:

        if(isinstance(obj[name], State)):
            data = {
                'state': obj[name].name,
                'id': obj[name].id
            }
            states.append(data)

    return render_template("7-states_list.html", n=len(states), states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
