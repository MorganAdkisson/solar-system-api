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
    response_body = []
    planets = Planets.query.all()
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
    planet = validate_planet_id(planet_id)
    return {
    "id": planet.id, 
    "name": planet.name, 
    "description": planet.description, 
    "num_moons": planet.num_moons
    }
