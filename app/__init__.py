from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(testing=False):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if testing == {"testing": True}:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TESTING_SQLALCHEMY_DATABASE_URI')
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    db.init_app(app)
    migrate.init_app(app, db)
    from .models.planets import Planets
    from .routes import planets_bp
    app.register_blueprint(planets_bp)

    return app
