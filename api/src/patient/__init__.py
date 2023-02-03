from flask import Blueprint

patient = Blueprint("patient", __name__, url_prefix="/api/client")

from src.patient import routes