from flask import Blueprint, jsonify, request
from src.config.db import db

pharmacy = Blueprint("pharmacy", __name__, url_prefix="/api/officine")