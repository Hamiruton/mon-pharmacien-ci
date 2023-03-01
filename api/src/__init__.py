from flask import Flask
from flask_cors import CORS

# Call Blueprints
from src.patient import patient
from src.pharmacy import pharmacy

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": ["http://localhost:8080"]}})

    # Load config
    app.config.from_prefixed_env()

    # Load Blueprints
    app.register_blueprint(patient)
    app.register_blueprint(pharmacy)

    return app

if __name__ == '__main__':
    create_app()