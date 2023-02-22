from flask import Blueprint, jsonify, request
from src.config.db import get_database

pharmacy = Blueprint("pharmacy", __name__, url_prefix="/api/officine")