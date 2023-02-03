from flask import Flask

# Call Blueprints
from src.auth import auth
from src.patient import patient
from src.pharmacy import pharmacy

def create_app():
    app = Flask(__name__)

    # Load config
    app.config.from_prefixed_env()

    # Load Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(patient)
    app.register_blueprint(pharmacy)

    return app