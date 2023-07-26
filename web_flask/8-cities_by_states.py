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


@app.route("/cities_by_states", strict_slashes=False)
def states_city_list():
    """ returns html with all the states & cities from the db """
    """
    states = sorted(list(storage.all(State).values()), key=lambda s: s.name)

    return render_template("8-cities_by_states.html", states=states)
    """

    states = storage.all(State).values()
    cities = storage.all(City).values()

    data = []
    for state in states:
        state_city = []
        state_data = {}
        for city in cities:
            if (state.id == city.state_id):
                state_city.append({
                    "name": city.name,
                    "id": city.id
                })

        state_data = {
            "name": state.name,
            "id": state.id,
            "cities": sorted(state_city, key=lambda x: x['name'])
        }
        data.append(state_data)
    print(data)
    return render_template("8-cities_by_states.html", data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
