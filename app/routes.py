from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planets import Planets

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")
@planets_bp.route("", methods=["POST"])
def create_planet():
    planets_response = request.get_json()
    new_planet = Planets(
        name = planets_response["name"],
        description = planets_response["description"],
        num_moons = planets_response["num_moons"]
    )

    db.session.add(new_planet)
    db.session.commit()
    return {
        "id": new_planet.id
    }, 201

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    params = request.args
    if "name" in params and "num_moons" in params:
        planet_name = params["name"]
        num_moons_value = params["num_moons"]
        planets = Planets.query.filter_by(name=planet_name, num_moons=num_moons_value)

    if "name" in params:
        planet_name = params["name"]
        planets = Planets.query.filter_by(name=planet_name)
    elif "num_moons" in params:
        num_moons_value = params["num_moons"]
        planets = Planets.query.filter_by(num_moons=num_moons_value)
    else:
        planets = Planets.query.all()

    response_body = []
    for planet in planets:
        response_body.append({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "num_moons": planet.num_moons
        })
    return jsonify(response_body)

def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"The planet id {planet_id} is invalid. The id must be integer."}, 400))
    planets = Planets.query.all()
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"message": f"The planet id {planet_id} is not found"}, 404))


@planets_bp.route("/<planet_id>", methods=["GET"])
def get_planet_by_id(planet_id):
    planet_request_body = validate_planet_id(planet_id)
    return {
    "id": planet_request_body.id, 
    "name": planet_request_body.name, 
    "description": planet_request_body.description, 
    "num_moons": planet_request_body.num_moons
    }

@planets_bp.route("/<planet_id>", methods=["PUT"])
def replace_one_planet(planet_id):
    planet = validate_planet_id(planet_id)
    planets_request = request.get_json()
    planet.name = planets_request["name"]
    planet.description = planets_request["description"]
    planet.num_moons = planets_request["num_moons"]

    db.session.commit()

    return jsonify({'msg': f"Successfully replaced planet with id {planet_id}"})

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_one_planet(planet_id):
    planet = validate_planet_id(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return jsonify({'msg': f"Deleted planet with id {planet_id}"})