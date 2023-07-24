#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
from models import *
from models import storage
import json

app = Flask(__name__)

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


@app.teardown_appcontext
def closeDbConnection(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
