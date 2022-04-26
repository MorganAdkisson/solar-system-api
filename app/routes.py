import json
from flask import Blueprint, jsonify, abort, make_response

class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons

planets = [
    Planet(1, "Mercury", "closest planet to the Sun", 0), 
    Planet(2, "Venus",  "second planet from the Sun", 0),
    Planet(3, "Earth",  "third planet from the Sun", 1),
    Planet(4, "Mars",  "brightness and closeness to Earth", 2), 
    Planet(5, "Jupiter",  "fifth planet from the Sun", 67), 
    Planet(6, "Saturn",  "sixth planet from the Sun", 62), 
    Planet(7, "Uranus",  "seventh planet from the Sun", 27), 
    Planet(8, "Neptune",  "farthest planet from the Sun", 14), 
    ]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET"])
def get_all_planets():
    planets_response = []
    for planet in planets:
        planets_response.append({
            "id": planet.id, 
            "name": planet.name, 
            "description": planet.description, 
            "num_moons": planet.num_moons
        })
    return jsonify(planets_response)

def validate_planet_id(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response({"message": f"The planet id {planet_id} is invalid. The id must be integer."}, 400))

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
