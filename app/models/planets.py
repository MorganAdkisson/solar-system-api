from app import db
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    num_moons = db.Column(db.Integer)
    


# class Planet:
#     def __init__(self, id, name, description, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_moons = num_moons

# planets = [
#     Planet(1, "Mercury", "closest planet to the Sun", 0), 
#     Planet(2, "Venus",  "second planet from the Sun", 0),
#     Planet(3, "Earth",  "third planet from the Sun", 1),
#     Planet(4, "Mars",  "brightness and closeness to Earth", 2), 
#     Planet(5, "Jupiter",  "fifth planet from the Sun", 67), 
#     Planet(6, "Saturn",  "sixth planet from the Sun", 62), 
#     Planet(7, "Uranus",  "seventh planet from the Sun", 27), 
#     Planet(8, "Neptune",  "farthest planet from the Sun", 14), 
#     ]