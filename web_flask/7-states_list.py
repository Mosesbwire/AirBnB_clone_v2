#!/usr/bin/python3
""" Flask web application """

from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)

@app.teardown_appcontext
def closeDbConnection(exception):
    """ close db connection after call """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ returns html with all the states from the db """
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)
    
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
