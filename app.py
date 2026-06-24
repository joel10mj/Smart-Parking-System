from flask import Flask, render_template, request
from parking import ParkingSystem

app = Flask(__name__)

parking = ParkingSystem(5)

@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        vehicle = request.form["vehicle"]
        vehicle_type = request.form["type"]

        if request.form["action"] == "park":
            message = parking.park_vehicle(vehicle, vehicle_type)

        elif request.form["action"] == "remove":
            message = parking.remove_vehicle(vehicle)

    slots = parking.get_status()

    return render_template("index.html", message=message, slots=slots)


if __name__ == "__main__":
    app.run(debug=True)